from unittest import TestCase

import numpy as np
from tc_core_analyzer_lib.assess_engagement import EngagementAssessment
from tc_core_analyzer_lib.utils.activity import DiscordActivity


class TestActionsAllActive(TestCase):
    def setUp(self) -> None:
        self.window_days = 7
        self.action_params = {
            "INT_THR": 1,
            "UW_DEG_THR": 1,
            "PAUSED_T_THR": 1,
            "CON_T_THR": 4,
            "CON_O_THR": 3,
            "EDGE_STR_THR": 5,
            "UW_THR_DEG_THR": 5,
            "VITAL_T_THR": 4,
            "VITAL_O_THR": 3,
            "STILL_T_THR": 2,
            "STILL_O_THR": 2,
            "DROP_H_THR": 2,
            "DROP_I_THR": 1,
        }

    def test_single_action_thr_msg(self):
        acc_names = []
        acc_count = 5
        for i in range(5):
            acc_names.append(f"user{i}")

        acc_names = np.array(acc_names)

        int_mat = {
            DiscordActivity.Reply: np.zeros((acc_count, acc_count)),
            DiscordActivity.Mention: np.zeros((acc_count, acc_count)),
            DiscordActivity.Reaction: np.zeros((acc_count, acc_count)),
            DiscordActivity.Lone_msg: np.zeros((acc_count, acc_count)),
            DiscordActivity.Thread_msg: np.zeros((acc_count, acc_count)),
        }

        int_mat[DiscordActivity.Thread_msg][1, 1] = 2

        activity_dict = {
            "all_joined": {"0": set()},
            "all_joined_day": {"0": set()},
            "all_consistent": {},
            "all_vital": {},
            "all_active": {},
            "all_connected": {},
            "all_paused": {},
            "all_new_disengaged": {},
            "all_disengaged": {},
            "all_unpaused": {},
            "all_returned": {},
            "all_new_active": {},
            "all_still_active": {},
            "all_dropped": {},
            "all_disengaged_were_newly_active": {},
            "all_disengaged_were_consistently_active": {},
            "all_disengaged_were_vital": {},
            "all_lurker": {},
            "all_about_to_disengage": {},
            "all_disengaged_in_past": {},
        }
        # window index
        w_i = 0

        activities = [
            DiscordActivity.Reaction,
            DiscordActivity.Mention,
            DiscordActivity.Reply,
            DiscordActivity.Lone_msg,
            DiscordActivity.Thread_msg,
        ]

        engagement = EngagementAssessment(
            activities=activities,
            activities_ignore_0_axis=[
                DiscordActivity.Mention,
                DiscordActivity.Reaction,
                DiscordActivity.Reply,
            ],
            activities_ignore_1_axis=[],
        )

        (_, *computed_activities) = engagement.compute(
            int_mat=int_mat,
            w_i=w_i,
            acc_names=acc_names,
            act_param=self.action_params,
            WINDOW_D=self.window_days,
            **activity_dict,
        )

        computed_activities = dict(zip(activity_dict.keys(), computed_activities))

        assert computed_activities["all_joined"] == {"0": set()}
        assert computed_activities["all_consistent"] == {"0": set()}
        assert computed_activities["all_vital"] == {"0": set()}
        assert computed_activities["all_active"] == {"0": set(["user1"])}
        assert computed_activities["all_connected"] == {"0": set()}
        assert computed_activities["all_dropped"] == {"0": set()}
        assert computed_activities["all_new_active"] == {"0": set(["user1"])}
        assert computed_activities["all_still_active"] == {"0": set()}
        assert computed_activities["all_paused"] == {"0": set()}
        assert computed_activities["all_returned"] == {"0": set()}
        assert computed_activities["all_unpaused"] == {"0": set()}
        assert computed_activities["all_new_disengaged"] == {"0": set()}
        assert computed_activities["all_disengaged"] == {"0": set()}
        assert computed_activities["all_disengaged_were_newly_active"] == {"0": set()}
        assert computed_activities["all_disengaged_were_consistently_active"] == {
            "0": set()
        }
        assert computed_activities["all_disengaged_were_vital"] == {"0": set()}
        assert computed_activities["all_lurker"] == {"0": set()}
        assert computed_activities["all_about_to_disengage"] == {"0": set()}
        assert computed_activities["all_disengaged_in_past"] == {"0": set()}

    def test_multiple_actions_thread_msg(self):
        acc_names = []
        acc_count = 5
        for i in range(5):
            acc_names.append(f"user{i}")

        acc_names = np.array(acc_names)

        int_mat = {
            DiscordActivity.Reply: np.zeros((acc_count, acc_count)),
            DiscordActivity.Mention: np.zeros((acc_count, acc_count)),
            DiscordActivity.Reaction: np.zeros((acc_count, acc_count)),
            DiscordActivity.Lone_msg: np.zeros((acc_count, acc_count)),
            DiscordActivity.Thread_msg: np.zeros((acc_count, acc_count)),
        }

        int_mat[DiscordActivity.Thread_msg][1, 1] = 2
        int_mat[DiscordActivity.Thread_msg][2, 2] = 3
        int_mat[DiscordActivity.Thread_msg][3, 3] = 1

        activity_dict = {
            "all_joined": {"0": set()},
            "all_joined_day": {"0": set()},
            "all_consistent": {},
            "all_vital": {},
            "all_active": {},
            "all_connected": {},
            "all_paused": {},
            "all_new_disengaged": {},
            "all_disengaged": {},
            "all_unpaused": {},
            "all_returned": {},
            "all_new_active": {},
            "all_still_active": {},
            "all_dropped": {},
            "all_disengaged_were_newly_active": {},
            "all_disengaged_were_consistently_active": {},
            "all_disengaged_were_vital": {},
            "all_lurker": {},
            "all_about_to_disengage": {},
            "all_disengaged_in_past": {},
        }
        # window index
        w_i = 0

        activities = [
            DiscordActivity.Reaction,
            DiscordActivity.Mention,
            DiscordActivity.Reply,
            DiscordActivity.Lone_msg,
            DiscordActivity.Thread_msg,
        ]

        engagement = EngagementAssessment(
            activities=activities,
            activities_ignore_0_axis=[
                DiscordActivity.Mention,
                DiscordActivity.Reaction,
                DiscordActivity.Reply,
            ],
            activities_ignore_1_axis=[],
        )

        (_, *computed_activities) = engagement.compute(
            int_mat=int_mat,
            w_i=w_i,
            acc_names=acc_names,
            act_param=self.action_params,
            WINDOW_D=self.window_days,
            **activity_dict,
        )

        computed_activities = dict(zip(activity_dict.keys(), computed_activities))

        assert computed_activities["all_joined"] == {"0": set()}
        assert computed_activities["all_consistent"] == {"0": set()}
        assert computed_activities["all_vital"] == {"0": set()}
        assert computed_activities["all_active"] == {
            "0": set(["user1", "user2", "user3"])
        }
        assert computed_activities["all_connected"] == {"0": set()}
        assert computed_activities["all_dropped"] == {"0": set()}
        assert computed_activities["all_new_active"] == {
            "0": set(["user1", "user2", "user3"])
        }
        assert computed_activities["all_still_active"] == {"0": set()}
        assert computed_activities["all_paused"] == {"0": set()}
        assert computed_activities["all_returned"] == {"0": set()}
        assert computed_activities["all_unpaused"] == {"0": set()}
        assert computed_activities["all_new_disengaged"] == {"0": set()}
        assert computed_activities["all_disengaged"] == {"0": set()}
        assert computed_activities["all_disengaged_were_newly_active"] == {"0": set()}
        assert computed_activities["all_disengaged_were_consistently_active"] == {
            "0": set()
        }
        assert computed_activities["all_disengaged_were_vital"] == {"0": set()}
        assert computed_activities["all_lurker"] == {"0": set()}
        assert computed_activities["all_about_to_disengage"] == {"0": set()}
        assert computed_activities["all_disengaged_in_past"] == {"0": set()}

    def test_single_action_thread_msg(self):
        acc_names = []
        acc_count = 5
        for i in range(5):
            acc_names.append(f"user{i}")

        acc_names = np.array(acc_names)

        int_mat = {
            DiscordActivity.Reply: np.zeros((acc_count, acc_count)),
            DiscordActivity.Mention: np.zeros((acc_count, acc_count)),
            DiscordActivity.Reaction: np.zeros((acc_count, acc_count)),
            DiscordActivity.Lone_msg: np.zeros((acc_count, acc_count)),
            DiscordActivity.Thread_msg: np.zeros((acc_count, acc_count)),
        }

        int_mat[DiscordActivity.Thread_msg][1, 1] = 2

        activity_dict = {
            "all_joined": {"0": set()},
            "all_joined_day": {"0": set()},
            "all_consistent": {},
            "all_vital": {},
            "all_active": {},
            "all_connected": {},
            "all_paused": {},
            "all_new_disengaged": {},
            "all_disengaged": {},
            "all_unpaused": {},
            "all_returned": {},
            "all_new_active": {},
            "all_still_active": {},
            "all_dropped": {},
            "all_disengaged_were_newly_active": {},
            "all_disengaged_were_consistently_active": {},
            "all_disengaged_were_vital": {},
            "all_lurker": {},
            "all_about_to_disengage": {},
            "all_disengaged_in_past": {},
        }
        # window index
        w_i = 0

        activities = [
            DiscordActivity.Reaction,
            DiscordActivity.Mention,
            DiscordActivity.Reply,
            DiscordActivity.Lone_msg,
            DiscordActivity.Thread_msg,
        ]

        engagement = EngagementAssessment(
            activities=activities,
            activities_ignore_0_axis=[
                DiscordActivity.Mention,
                DiscordActivity.Reaction,
                DiscordActivity.Reply,
            ],
            activities_ignore_1_axis=[],
        )

        (_, *computed_activities) = engagement.compute(
            int_mat=int_mat,
            w_i=w_i,
            acc_names=acc_names,
            act_param=self.action_params,
            WINDOW_D=self.window_days,
            **activity_dict,
        )

        computed_activities = dict(zip(activity_dict.keys(), computed_activities))

        assert computed_activities["all_joined"] == {"0": set()}
        assert computed_activities["all_consistent"] == {"0": set()}
        assert computed_activities["all_vital"] == {"0": set()}
        assert computed_activities["all_active"] == {"0": set(["user1"])}
        assert computed_activities["all_connected"] == {"0": set()}
        assert computed_activities["all_dropped"] == {"0": set()}
        assert computed_activities["all_new_active"] == {"0": set(["user1"])}
        assert computed_activities["all_still_active"] == {"0": set()}
        assert computed_activities["all_paused"] == {"0": set()}
        assert computed_activities["all_returned"] == {"0": set()}
        assert computed_activities["all_unpaused"] == {"0": set()}
        assert computed_activities["all_new_disengaged"] == {"0": set()}
        assert computed_activities["all_disengaged"] == {"0": set()}
        assert computed_activities["all_disengaged_were_newly_active"] == {"0": set()}
        assert computed_activities["all_disengaged_were_consistently_active"] == {
            "0": set()
        }
        assert computed_activities["all_disengaged_were_vital"] == {"0": set()}
        assert computed_activities["all_lurker"] == {"0": set()}
        assert computed_activities["all_about_to_disengage"] == {"0": set()}
        assert computed_activities["all_disengaged_in_past"] == {"0": set()}
