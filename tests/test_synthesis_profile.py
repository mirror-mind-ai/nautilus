from __future__ import annotations

import unittest
from pathlib import Path

import yaml

ROOT = Path(__file__).resolve().parents[1]
PROFILE = ROOT / "runtime" / "synthesis-profile.yaml"


class SynthesisProfileTests(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.profile = yaml.safe_load(PROFILE.read_text(encoding="utf-8"))

    def test_profile_is_versioned_against_mirror_and_protocol(self):
        self.assertEqual("1.0", self.profile["profile_version"])
        self.assertEqual("mirror.journey-projections@1.0", self.profile["mirror_contract"])
        self.assertEqual("1", self.profile["protocol_schema_version"])
        self.assertEqual("nautilus-synthesis", self.profile["extension_namespace"])

    def test_shared_policy_requires_sources_and_preserves_ambiguity(self):
        shared = self.profile["shared"]
        self.assertTrue(shared["source_policy"]["require_operational_snapshot"])
        self.assertTrue(shared["source_policy"]["require_source_references"])
        self.assertIn("Preserve uncertainty", shared["ambiguity_policy"])
        self.assertIn("Pi produces a candidate", shared["publication_policy"])

    def test_tactical_keeps_mission_evidence_and_deliveries_related(self):
        tactical = self.profile["tactical"]
        self.assertTrue(tactical["output_constraints"]["one_primary_mission"])
        self.assertTrue(tactical["output_constraints"]["evidence_must_support_mission"])
        self.assertTrue(tactical["output_constraints"]["deliverables_must_reference_evidence"])
        self.assertTrue(tactical["output_constraints"]["no_task_management"])

    def test_strategic_preserves_realization_impact_and_equal_value_lenses(self):
        strategic = self.profile["strategic"]
        constraints = strategic["output_constraints"]
        self.assertTrue(constraints["realization_is_primary"])
        self.assertTrue(constraints["impacts_must_reference_realization"])
        self.assertTrue(constraints["value_lenses_have_equal_weight"])
        self.assertTrue(constraints["value_lenses_are_not_scores"])
        self.assertIn("after realized value", strategic["impact"]["meaning"])

    def test_all_intent_has_causal_execution_order(self):
        self.assertEqual(
            [
                "rebuild-operational-deterministically",
                "synthesize-tactical-from-current-operational",
                "synthesize-strategic-from-current-operational-and-current-tactical",
                "publish-through-validated-extension-boundary",
            ],
            self.profile["execution_order"]["all"],
        )

    def test_profile_excludes_scoring_and_implicit_invocation(self):
        forbidden = self.profile["shared"]["forbidden_patterns"]
        self.assertIn("scores", forbidden)
        self.assertIn("implicit-provider-invocation", forbidden)


if __name__ == "__main__":
    unittest.main()
