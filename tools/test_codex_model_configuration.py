"""Keep the actual Codex picker and staged-role configuration compatible."""
import json
from pathlib import Path
import unittest

class CodexModelConfigurationTests(unittest.TestCase):
    def test_picker_candidates_can_execute_in_every_codex_role(self):
        data = json.loads((Path(__file__).resolve().parents[1] / "traceability/manifest.json").read_text())
        execution = data["development_execution"]
        provider = next(p for p in execution["agent_providers"] if p["id"] == "codex")
        self.assertTrue(execution["allow_model_selection"])
        self.assertTrue(provider["allow_model_selection"])
        ids = [m["id"] for m in provider["model_candidates"]]
        self.assertEqual(len(ids), len(set(ids)))
        self.assertIn("default", ids)
        named = set(ids) - {"default"}
        self.assertTrue(named, "Refresh must probe named Codex models")
        for name, role in data["agent_roles"].items():
            with self.subTest(role=name):
                codex = role["providers"]["codex"]
                self.assertTrue(named <= set(codex["models"]))
                self.assertEqual(codex["model_argument"], ["--model", "{model}"])
                self.assertIn("--sandbox", codex["command"])

if __name__ == "__main__":
    unittest.main()
