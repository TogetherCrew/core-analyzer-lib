import unittest

from tc_core_analyzer_lib.utils.assessments.assess_inconsistent import (
    assess_inconsistent,
)


class TestAssessInconsistent(unittest.TestCase):
    def test_inconsistent_members_empty_inputs(self):
        all_active = {"0": set()}
        all_paused = {"0": set()}
        all_new_active = {"0": set()}
        all_consistent = {"0": set()}

        all_inconsistent = assess_inconsistent(
            all_active=all_active,
            all_paused=all_paused,
            all_new_active=all_new_active,
            all_consistent=all_consistent,
            w_i=0,
        )

        self.assertEqual(all_inconsistent, set())

    def test_inconsistent_members_paused_members(self):
        all_active = {"0": set(["User1", "User2"])}
        all_paused = {"0": set(["User3", "User4"])}
        all_new_active = {"0": set(["User1", "User2"])}
        all_consistent = {"0": set()}

        all_inconsistent = assess_inconsistent(
            all_active=all_active,
            all_paused=all_paused,
            all_new_active=all_new_active,
            all_consistent=all_consistent,
            w_i=0,
        )

        self.assertEqual(all_inconsistent, set(["User3", "User4"]))

    def test_inconsistent_members_active_members(self):
        all_active = {"0": set(["User1", "User2"]), "1": set(["User1", "User2"])}
        all_paused = {"0": set(["User3", "User4"]), "1": set()}
        all_new_active = {
            "0": set(["User1", "User2"]),
            "1": set([]),
        }
        all_consistent = {"0": set(), "1": set()}

        all_inconsistent = assess_inconsistent(
            all_active=all_active,
            all_paused=all_paused,
            all_new_active=all_new_active,
            all_consistent=all_consistent,
            w_i=1,
        )

        self.assertEqual(all_inconsistent, set(["User1", "User2"]))
