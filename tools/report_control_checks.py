#!/usr/bin/env python3
"""Report baseline validation, control unit tests and GUI manifest ingestion."""
import json
import os
from pathlib import Path
import sys
import time

from report_support import case, command, destinations, python_cases, report_artifacts, write_report


ROOT = Path(__file__).resolve().parents[1]


def ingestion(root, artifacts):
    for label in ('gui-import', 'gui-ingestion'):
        for suffix in ('.stdout.log', '.stderr.log'):
            (artifacts / (label + suffix)).unlink(missing_ok=True)
    started = time.perf_counter()
    manifest = root / 'traceability/manifest.json'
    try:
        data = json.loads(manifest.read_text())
        matches = [r for r in data['repositories'] if r['id'] == 'gui']
        if len(matches) != 1:
            raise ValueError('Manifest must register exactly one GUI repository')
        source = (root / matches[0]['path'] / 'src').resolve()
        if not all((source / 'sdlc_gui' / name).is_file()
                   for name in ('__init__.py', '__main__.py')):
            raise ValueError('Manifest-resolved GUI package is unavailable')
    except (OSError, ValueError, KeyError, TypeError) as exc:
        return case('gui-ingestion', 'error', time.perf_counter() - started, str(exc))
    env = dict(os.environ)
    # Do not fall back to another installed GUI or inherited source checkout.
    env['PYTHONPATH'] = str(source)
    # Import the entry point without invoking its guarded CLI. This separates
    # an unusable package/dependency from a rejected manifest. Safe-path mode
    # prevents a package in the control working directory shadowing this source.
    result, _ = command([sys.executable, '-P', '-c', 'import sdlc_gui.__main__'],
                        root, artifacts, 'gui-import', env)
    if result is None or result.returncode != 0:
        return case('gui-ingestion', 'error', time.perf_counter() - started,
                    'Manifest-resolved GUI package is unavailable; see gui-import logs')
    _, outcome = command([sys.executable, '-P', '-m', 'sdlc_gui', '--manifest',
                           str(manifest), '--validate-only'], root, artifacts, 'gui-ingestion', env)
    outcome['duration_seconds'] = time.perf_counter() - started
    return outcome


def main(root=ROOT):
    output, artifacts = destinations(root)
    _, baseline = command([sys.executable, str(root / 'tools/validate_business_baseline.py')],
                          root, artifacts, 'business-baseline')
    cases = [baseline, *python_cases(root, root / 'tools', artifacts), ingestion(root, artifacts)]
    return write_report(output, cases, report_artifacts(
        artifacts, ['business-baseline', 'python', 'gui-import', 'gui-ingestion']))


if __name__ == '__main__':
    raise SystemExit(main())
