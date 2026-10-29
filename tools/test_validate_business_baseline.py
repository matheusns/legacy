"""Exercise baseline validation against isolated candidate/lifecycle fixtures."""
import json
from pathlib import Path
import shutil
import subprocess
import sys
import tempfile
import unittest


class BusinessBaselineValidationTests(unittest.TestCase):
    def setUp(self):
        self.temp = tempfile.TemporaryDirectory()
        self.addCleanup(self.temp.cleanup)
        self.root = Path(self.temp.name)
        (self.root / 'tools').mkdir()
        (self.root / 'traceability').mkdir()
        shutil.copyfile(Path(__file__).with_name('validate_business_baseline.py'),
                        self.root / 'tools/validate_business_baseline.py')
        (self.root / 'work.md').write_text('# Work package\n')
        self.manifest = {
            'schema_version': 2, 'project': {},
            'requirements': [{'id': 'REQ-1', 'statement': 'A candidate requirement',
                              'status': 'Candidate', 'functionality_ids': ['CAP-1']}],
            'functionalities': [{'id': 'CAP-1', 'requirement_ids': ['REQ-1']}],
            'work_packages': [{'id': 'WORK-1', 'status': 'Backlog', 'path': 'work.md',
                               'functionality_ids': ['CAP-1'], 'target_repositories': ['matheusns/legacy']}],
            'artifacts': [{'id': 'ART-1', 'path': 'work.md'}],
        }
        self.baseline = {
            'use_cases': [{'id': 'UC-1', 'requirements': ['REQ-1'],
                           'main_flow': ['Act'], 'alternate_flows': ['Recover']}],
            'verification_definitions': [{'id': 'FVT-1', 'requirement_ids': ['REQ-1'], 'status': 'Planned'}],
        }

    def validate(self):
        manifest = self.root / 'traceability/manifest.json'
        manifest.write_text(json.dumps(self.manifest))
        (self.root / 'traceability/business_baseline.json').write_text(json.dumps(self.baseline))
        before = manifest.read_bytes()
        result = subprocess.run([sys.executable, str(self.root / 'tools/validate_business_baseline.py')],
                                text=True, capture_output=True)
        self.assertEqual(manifest.read_bytes(), before, 'Validation must not rewrite lifecycle or approval')
        return result

    def test_work_can_progress_without_promoting_candidate_requirements(self):
        for status in ('Backlog', 'In Development', 'In Progress', 'In Review',
                       'Blocked', 'Deferred', 'Done', 'Archived'):
            with self.subTest(status=status):
                self.manifest['work_packages'][0]['status'] = status
                result = self.validate()
                self.assertEqual(result.returncode, 0, result.stderr)
                self.assertEqual(self.manifest['requirements'][0]['status'], 'Candidate')

    def test_unknown_or_missing_status_identifies_the_work_package(self):
        for status in ('Dnoe', '', None):
            with self.subTest(status=status):
                self.manifest['work_packages'][0]['status'] = status
                result = self.validate()
                self.assertNotEqual(result.returncode, 0)
                self.assertIn('Invalid work package status for WORK-1', result.stderr)

    def test_done_does_not_bypass_dependency_integrity(self):
        self.manifest['work_packages'][0].update(status='Done', depends_on=['MISSING'])
        self.assertNotEqual(self.validate().returncode, 0)

    def test_done_does_not_bypass_missing_control_document(self):
        self.manifest['work_packages'][0].update(status='Done', path='missing.md')
        result = self.validate()
        self.assertNotEqual(result.returncode, 0)
        self.assertIn('Missing WP document', result.stderr)

    def test_done_does_not_approve_requirements(self):
        self.manifest['work_packages'][0]['status'] = 'Done'
        self.manifest['requirements'][0]['status'] = 'Approved'
        result = self.validate()
        self.assertNotEqual(result.returncode, 0)
        self.assertIn('Unexpected approval status: REQ-1', result.stderr)

    def test_cycle_is_still_rejected_after_completion(self):
        self.manifest['work_packages'][0].update(status='Done', depends_on=['WORK-1'])
        result = self.validate()
        self.assertNotEqual(result.returncode, 0)
        self.assertIn('work package dependency cycle', result.stderr)


if __name__ == '__main__':
    unittest.main()
