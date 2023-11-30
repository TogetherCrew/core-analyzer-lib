import numpy as np
from tc_core_analyzer_lib.assess_engagement import EngagementAssessment
from tc_core_analyzer_lib.utils.activity import DiscordActivity


def test_mention_active_members_from_int_matrix():
    """
    test whether the people are being mentioned are active or not
    the shouldn't considered as active as we're not counting them
    the interaction matrix is the starting point
    """
    acc_names = []
    acc_count = 5

    act_param = {
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

    for i in range(5):
        acc_names.append(f"user{i}")

    acc_names = np.array(acc_names)

    # 28 weeks
    max_interval = 28

    # preparing empty joined members dict
    all_joined = dict(
        zip(np.array(range(max_interval), dtype=str), np.repeat(set(), max_interval))
    )

    activity_dict = {
        "all_joined": {},
        "all_joined_day": all_joined,
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
    memberactivities = activity_dict.keys()

    int_mat = {
        DiscordActivity.Reply: np.zeros((acc_count, acc_count)),
        DiscordActivity.Mention: np.zeros((acc_count, acc_count)),
        DiscordActivity.Reaction: np.zeros((acc_count, acc_count)),
    }

    # `user_0` mentioning `user_1`
    int_mat[DiscordActivity.Mention][0, 1] = 2

    activities = [
        DiscordActivity.Reaction,
        DiscordActivity.Mention,
        DiscordActivity.Reply,
    ]
    engagement = EngagementAssessment(
        activities=activities,
        activities_ignore_0_axis=[DiscordActivity.Mention],
        activities_ignore_1_axis=[],
    )

    # the analytics
    for w_i in range(max_interval):
        # time window
        WINDOW_D = 7

        (_, *activity_dict) = engagement.compute(
            int_mat=int_mat,
            w_i=w_i,
            acc_names=acc_names,
            act_param=act_param,
            WINDOW_D=WINDOW_D,
            **activity_dict,
        )

        activity_dict = dict(zip(memberactivities, activity_dict))
        # zeroing it on the day 7
        # we should have it all_disengaged_were_newly_active in day 7 + 7
        if w_i == 6:
            int_mat[DiscordActivity.Mention][0, 1] = 0

    print("all_new_active:", activity_dict["all_new_active"])

    assert activity_dict["all_active"] == {
        "0": {"user0"},
        "1": {"user0"},
        "2": {"user0"},
        "3": {"user0"},
        "4": {"user0"},
        "5": {"user0"},
        "6": {"user0"},
        "7": set(),
        "8": set(),
        "9": set(),
        "10": set(),
        "11": set(),
        "12": set(),
        "13": set(),
        "14": set(),
        "15": set(),
        "16": set(),
        "17": set(),
        "18": set(),
        "19": set(),
        "20": set(),
        "21": set(),
        "22": set(),
        "23": set(),
        "24": set(),
        "25": set(),
        "26": set(),
        "27": set(),
    }
