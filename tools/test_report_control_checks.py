"""Control wrapper fixtures do not invoke the enclosing control discovery."""
import json
import os
from pathlib import Path
import shutil
import subprocess
import sys
import tempfile
import unittest
from unittest.mock import patch

import report_control_checks as wrapper
import report_support as support


class ControlReportTests(unittest.TestCase):
    def setUp(self):
        self.temp = tempfile.TemporaryDirectory()
        self.addCleanup(self.temp.cleanup)
        self.root = Path(self.temp.name)
        self.tools = self.root / 'tools'
        self.tools.mkdir()
        self.artifacts = self.root / 'artifacts'
        self.artifacts.mkdir()
        (self.root / 'traceability').mkdir()
        self.manifest = self.root / 'traceability/manifest.json'
        self.manifest.write_text(json.dumps({'repositories': [{'id': 'gui', 'path': 'gui'}]}))
        package = self.root / 'gui/src/sdlc_gui'
        package.mkdir(parents=True)
        (package / '__init__.py').write_text('')
        (package / '__main__.py').write_text('')
        self.validator = self.tools / 'validate_business_baseline.py'
        self.validator.write_text('')
        self.fixture = self.tools / 'test_fixture.py'
        self.fixture.write_text('import unittest\nclass Cases(unittest.TestCase):\n    def test_ok(self): pass\n')
        self.output = self.root / 'custom/result.json'

    def run_wrapper(self):
        with patch.dict(os.environ, {'SDLC_RESULT_PATH': str(self.output),
                                     'SDLC_ARTIFACT_DIR': str(self.artifacts)}):
            status = wrapper.main(self.root)
        report = json.loads(self.output.read_text())
        self.assertEqual(report['schema_version'], 1)
        self.assertEqual(report['metrics'], {})
        self.assertIn(str(self.artifacts / 'python-version.txt'), report['artifacts'])
        self.assertTrue(all(Path(p).is_file() for p in report['artifacts']))
        self.assertFalse((self.root / 'test-results/result.json').exists())
        self.assertEqual(len({c['name'] for c in report['tests']}), len(report['tests']))
        self.assertTrue(all(c['duration_seconds'] >= 0 for c in report['tests']))
        return status, report['tests']

    def test_pass_and_validator_failure(self):
        status, cases = self.run_wrapper()
        self.assertEqual(status, 0)
        self.assertEqual([c['status'] for c in cases], ['passed'] * 3)
        self.validator.write_text("raise AssertionError('invalid baseline')\n")
        status, cases = self.run_wrapper()
        self.assertEqual(status, 1)
        self.assertEqual(cases[0]['status'], 'failed')

    def test_unittest_failure_error_skip_and_subtest(self):
        self.fixture.write_text('''import unittest
class Cases(unittest.TestCase):
    def test_fail(self): self.fail('bad')
    def test_error(self): raise ValueError('bad')
    @unittest.skip('fixture')
    def test_skip(self): pass
    def test_subtest(self):
        with self.subTest(x=1): self.fail('subtest')
''')
        status, cases = self.run_wrapper()
        self.assertEqual(status, 1)
        self.assertEqual(sorted(c['status'] for c in cases[1:-1]), ['error', 'failed', 'failed', 'skipped'])

    def test_empty_discovery_and_missing_python(self):
        self.fixture.unlink()
        status, cases = self.run_wrapper()
        self.assertEqual(status, 1)
        self.assertEqual(cases[1]['status'], 'error')
        with patch.object(sys, 'executable', str(self.root / 'missing-python')):
            status, cases = self.run_wrapper()
        self.assertEqual(status, 1)
        self.assertTrue(all(c['status'] == 'error' for c in cases))

    def test_missing_gui_is_error_even_with_inherited_package(self):
        shutil.rmtree(self.root / 'gui')
        case = wrapper.ingestion(self.root, self.artifacts)
        self.assertEqual(case['status'], 'error')
        self.assertIn('unavailable', case['message'])

    def test_invalid_manifest_rejected_by_real_gui(self):
        # Resolve the allocated GUI from the real manifest, not a sibling guess.
        control = Path(__file__).resolve().parents[1]
        real = json.loads((control / 'traceability/manifest.json').read_text())
        entry = next(r for r in real['repositories'] if r['id'] == 'gui')
        source = (control / entry['path']).resolve()
        self.manifest.write_text(json.dumps({'schema_version': 999,
                                            'repositories': [{'id': 'gui', 'path': str(source)}]}))
        case = wrapper.ingestion(self.root, self.artifacts)
        self.assertEqual(case['status'], 'failed')
        self.assertTrue((self.artifacts / 'gui-ingestion.stderr.log').is_file())

    def test_existing_unimportable_gui_is_error(self):
        package = self.root / 'gui/src/sdlc_gui'
        for filename, body in (
                ('__init__.py', 'import missing_gui_fixture_dependency\n'),
                ('__main__.py', 'raise ImportError("broken entry point")\n'),
                ('__main__.py', 'invalid syntax here!\n')):
            with self.subTest(filename=filename, body=body):
                (package / '__init__.py').write_text('')
                (package / '__main__.py').write_text('')
                (package / filename).write_text(body)
                status, cases = self.run_wrapper()
                self.assertEqual(status, 1)
                self.assertEqual(cases[-1]['status'], 'error')
                self.assertIn('unavailable', cases[-1]['message'])
                report = json.loads(self.output.read_text())
                self.assertIn(str(self.artifacts / 'gui-import.stderr.log'), report['artifacts'])
                self.assertFalse((self.artifacts / 'gui-ingestion.stdout.log').exists())

    def test_control_directory_cannot_shadow_manifest_gui(self):
        shadow = self.root / 'sdlc_gui'
        shadow.mkdir()
        (shadow / '__init__.py').write_text('raise RuntimeError("wrong checkout")\n')
        status, cases = self.run_wrapper()
        self.assertEqual(status, 0)
        self.assertEqual(cases[-1]['status'], 'passed')

    def test_report_consumable_by_gui(self):
        control = Path(__file__).resolve().parents[1]
        data = json.loads((control / 'traceability/manifest.json').read_text())
        gui = next(r for r in data['repositories'] if r['id'] == 'gui')
        sys.path.insert(0, str((control / gui['path'] / 'src').resolve()))
        self.addCleanup(sys.path.pop, 0)
        from sdlc_gui.execution import read_report
        self.run_wrapper()
        report = read_report(self.output, {})
        self.assertEqual(report['tests']['total'], 3)
        self.assertIn(str(self.artifacts / 'gui-ingestion.stdout.log'), report['artifacts'])

    def test_fallback_destinations(self):
        with patch.dict(os.environ, {}, clear=True):
            self.assertEqual(wrapper.main(self.root), 0)
        output = self.root / 'test-results/result.json'
        report = json.loads(output.read_text())
        self.assertEqual(report['schema_version'], 1)
        self.assertTrue(all(Path(p).is_file() for p in report['artifacts']))

    def test_bounded_messages_preserve_full_error_log(self):
        self.fixture.write_text("import unittest\nclass Cases(unittest.TestCase):\n"
                                "    def test_long(self): raise ValueError('x' * 6000 + 'END_MARKER')\n")
        status, cases = self.run_wrapper()
        self.assertEqual(status, 1)
        self.assertEqual(cases[1]['status'], 'error')
        self.assertLessEqual(len(cases[1]['message']), 4000)
        self.assertIn('truncated', cases[1]['message'])
        self.assertIn('END_MARKER', (self.artifacts / 'python.stderr.log').read_text())

    def test_unavailable_ingestion_does_not_reference_stale_logs(self):
        self.run_wrapper()
        shutil.rmtree(self.root / 'gui')
        self.run_wrapper()
        report = json.loads(self.output.read_text())
        self.assertFalse(any('gui-ingestion.' in p for p in report['artifacts']))
        self.assertFalse(any('gui-import.' in p for p in report['artifacts']))

    def test_malformed_worker_reports_are_error_cases(self):
        valid = support.case('fixture', 'passed', 0.01)
        reports = [None, [], {}, {'schema_version': 2, 'tests': [valid]},
                   {'schema_version': 1, 'tests': {}},
                   {'schema_version': 1, 'tests': []}]
        invalid_cases = [None, {}, dict(valid, name=[]), dict(valid, name=' '),
                         dict(valid, status='unknown'), dict(valid, duration_seconds=True),
                         dict(valid, duration_seconds=-1), dict(valid, duration_seconds=float('nan')),
                         dict(valid, message=[])]
        reports.extend({'schema_version': 1, 'tests': [item]} for item in invalid_cases)
        reports.append({'schema_version': 1, 'tests': [valid, valid]})
        for report in reports:
            with self.subTest(report=report):
                def worker(*args, **kwargs):
                    (self.artifacts / 'python-tests.json').write_text(json.dumps(report))
                    return subprocess.CompletedProcess([], 0), support.case('python', 'passed', 0.01)
                with patch.object(support, 'command', side_effect=worker):
                    cases = support.python_cases(self.root, self.root, self.artifacts)
                self.assertEqual(len(cases), 1)
                self.assertEqual(cases[0]['status'], 'error')
                self.assertEqual(support.write_report(self.root / 'invalid.json', cases), 1)

    def test_worker_nonzero_exit_cannot_report_success(self):
        def worker(*args, **kwargs):
            support.write_report(self.artifacts / 'python-tests.json',
                                 [support.case('fixture', 'passed', 0.01)])
            return subprocess.CompletedProcess([], 2), support.case('python', 'failed', 0.02)
        with patch.object(support, 'command', side_effect=worker):
            cases = support.python_cases(self.root, self.root, self.artifacts)
        self.assertEqual([item['status'] for item in cases], ['passed', 'error'])
        self.assertEqual(support.write_report(self.root / 'nonzero.json', cases), 1)
