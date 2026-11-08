"""Standard-library report plumbing, mirrored in the GUI and control tools.

Keep the copies identical: control reporting must work when the GUI is absent.
Runner errors are explicitly named infrastructure cases, never passing tests.
"""
import json
import math
import os
from pathlib import Path
import subprocess
import sys
import time
import unittest


MESSAGE_LIMIT = 4000


def bounded_message(message):
    text = str(message)
    marker = '\n[truncated; see runner logs]'
    return text if len(text) <= MESSAGE_LIMIT else text[:MESSAGE_LIMIT - len(marker)] + marker


def case(name, status, duration, message=''):
    return dict(name=name, status=status, duration_seconds=duration, message=bounded_message(message))


class RecordingResult(unittest.TextTestResult):
    """One case per test method; subtest failures aggregate into that method."""

    def __init__(self, *args):
        super().__init__(*args)
        self.cases = []
        self.active = None
        self.started = time.perf_counter()
        self.current = None

    def startTest(self, test):
        super().startTest(test)
        self.active = test
        self.started = time.perf_counter()
        self.current = case(test.id(), 'passed', 0)

    def record(self, test, status, message=''):
        if self.active is not None:
            ranks = {'passed': 0, 'skipped': 1, 'failed': 2, 'error': 3}
            if ranks[status] > ranks[self.current['status']]:
                self.current['status'] = status
            self.current['message'] = bounded_message(self.current['message'] + message)
        else:
            # setUpClass/setUpModule/tearDownClass failures have no startTest.
            self.cases.append(case(test.id(), status,
                                   time.perf_counter() - self.started, message))

    def stopTest(self, test):
        self.current['duration_seconds'] = time.perf_counter() - self.started
        self.cases.append(self.current)
        self.active = None
        super().stopTest(test)

    def addFailure(self, test, err):
        super().addFailure(test, err)
        self.record(test, 'failed', self._exc_info_to_string(err, test))

    def addError(self, test, err):
        super().addError(test, err)
        self.record(test, 'error', self._exc_info_to_string(err, test))

    def addSkip(self, test, reason):
        super().addSkip(test, reason)
        self.record(test, 'skipped', reason)

    def addExpectedFailure(self, test, err):
        super().addExpectedFailure(test, err)
        self.record(test, 'skipped', 'Expected failure: ' + self._exc_info_to_string(err, test))

    def addUnexpectedSuccess(self, test):
        super().addUnexpectedSuccess(test)
        self.record(test, 'failed', 'Unexpected success')

    def addSubTest(self, test, subtest, err):
        super().addSubTest(test, subtest, err)
        if err is not None:
            status = 'failed' if issubclass(err[0], test.failureException) else 'error'
            self.record(test, status, str(subtest) + '\n' + self._exc_info_to_string(err, test))


def write_report(path, cases, artifacts=()):
    # Ordinals distinguish repeated test IDs/names without discarding real cases.
    tests = [dict(item, name=f'{index}: {item["name"]}',
                  message=bounded_message(item.get('message', '')))
             for index, item in enumerate(cases, 1)]
    path = Path(path)
    path.parent.mkdir(parents=True, exist_ok=True)
    temporary = path.with_name(path.name + '.tmp')
    temporary.write_text(json.dumps({'schema_version': 1, 'tests': tests,
                                     'metrics': {}, 'artifacts': [str(p) for p in artifacts]}, indent=2, allow_nan=False) + '\n')
    temporary.replace(path)
    return int(not tests or any(t['status'] in ('failed', 'error') for t in tests))


def unittest_worker(directory, output):
    started = time.perf_counter()
    try:
        suite = unittest.TestLoader().discover(str(directory), pattern='test_*.py')
        result = unittest.TextTestRunner(verbosity=2, resultclass=RecordingResult).run(suite)
        cases = result.cases
        if not cases:
            cases = [case('python discovery', 'error', time.perf_counter() - started,
                          'No tests discovered')]
    except Exception as exc:
        cases = [case('python runner', 'error', time.perf_counter() - started, repr(exc))]
    return write_report(output, cases)


def command(argv, root, artifacts, label, env=None):
    started = time.perf_counter()
    try:
        result = subprocess.run(argv, cwd=root, env=env, text=True,
                                stdout=subprocess.PIPE, stderr=subprocess.PIPE)
    except OSError as exc:
        (artifacts / (label + '.stdout.log')).write_text('')
        (artifacts / (label + '.stderr.log')).write_text(str(exc) + '\n')
        return None, case(label, 'error', time.perf_counter() - started, str(exc))
    (artifacts / (label + '.stdout.log')).write_text(result.stdout)
    (artifacts / (label + '.stderr.log')).write_text(result.stderr)
    return result, case(label, 'passed' if result.returncode == 0 else 'failed',
                        time.perf_counter() - started,
                        '' if result.returncode == 0 else f'Exit status {result.returncode}; see {label} logs')


def validate_cases(report):
    """Reject malformed worker output before it can enter the final report."""
    if (not isinstance(report, dict) or report.get('schema_version') != 1
            or not isinstance(report.get('tests'), list)):
        raise ValueError('Expected schema-version-1 test worker report')
    cases = report['tests']
    if not cases:
        raise ValueError('Empty test worker report')
    names = set()
    for item in cases:
        if not isinstance(item, dict):
            raise ValueError('Invalid test case')
        name = item.get('name')
        duration = item.get('duration_seconds')
        if not isinstance(name, str) or not name.strip() or name in names:
            raise ValueError('Test case names must be nonempty and unique')
        names.add(name)
        if item.get('status') not in ('passed', 'failed', 'error', 'skipped'):
            raise ValueError('Invalid test case status')
        if (not isinstance(duration, (int, float)) or isinstance(duration, bool)
                or not math.isfinite(duration) or duration < 0):
            raise ValueError('Invalid test case duration')
        if not isinstance(item.get('message', ''), str):
            raise ValueError('Invalid test case message')
    return cases


def python_cases(root, directory, artifacts):
    output = artifacts / 'python-tests.json'
    output.unlink(missing_ok=True)
    env = dict(os.environ)
    env['PYTHONPATH'] = str(root / 'src') + os.pathsep + env.get('PYTHONPATH', '')
    result, outcome = command([sys.executable, str(Path(__file__).resolve()),
                               str(directory), str(output)], root, artifacts, 'python', env)
    try:
        report = json.loads(output.read_text())
        cases = validate_cases(report)
    except (OSError, ValueError, KeyError) as exc:
        return [dict(outcome, status='error', message=f'Unittest worker report unavailable: {exc}')]
    if result is None or (result.returncode and not any(c['status'] in ('failed', 'error') for c in cases)):
        cases.append(dict(outcome, status='error'))
    return cases


def report_artifacts(artifacts, labels):
    paths = [artifacts / 'python-version.txt', artifacts / 'python-tests.json']
    paths.extend(artifacts / (label + suffix) for label in labels
                 for suffix in ('.stdout.log', '.stderr.log'))
    return [path for path in paths if path.is_file()]


def destinations(root, fallback='test-results/result.json'):
    output = Path(os.environ.get('SDLC_RESULT_PATH', root / fallback)).resolve()
    artifacts = Path(os.environ.get('SDLC_ARTIFACT_DIR', root / 'test-results/artifacts')).resolve()
    artifacts.mkdir(parents=True, exist_ok=True)
    (artifacts / 'python-version.txt').write_text(sys.version + '\n')
    return output, artifacts


if __name__ == '__main__':
    raise SystemExit(unittest_worker(Path(sys.argv[1]), Path(sys.argv[2])))
