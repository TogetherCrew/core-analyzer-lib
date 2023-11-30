import numpy as np
from tc_core_analyzer_lib.assess_engagement import EngagementAssessment
from tc_core_analyzer_lib.utils.activity import DiscordActivity


def test_all_active_fourteen_period():
    """
    test the all active category for past 14 periods

    The interaction matrix is the represantative of window_d days
    so we should have the users as active for the interaction matrix
    and not the window_d period here
    """
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

    analytics_length = 14
    all_joined_day = dict(
        zip(
            np.array(range(analytics_length), dtype=str),
            np.repeat(set(), analytics_length),
        )
    )

    activity_dict = {
        "all_joined": {},
        "all_joined_day": all_joined_day,
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

    WINDOW_D = 7

    acc_names = np.array(
        [
            "user0",
            "user1",
            "user2",
            "user3",
        ]
    )
    acc_count = len(acc_names)

    int_mat = {
        DiscordActivity.Reply: np.zeros((acc_count, acc_count)),
        DiscordActivity.Mention: np.zeros((acc_count, acc_count)),
        DiscordActivity.Reaction: np.zeros((acc_count, acc_count)),
    }

    # from day zero user0 and user1 are active
    int_mat[DiscordActivity.Reaction][0, 1] = 1
    int_mat[DiscordActivity.Reaction][1, 0] = 2

    activities = [
        DiscordActivity.Reaction,
        DiscordActivity.Mention,
        DiscordActivity.Reply,
    ]

    engagement = EngagementAssessment(
        activities=activities, activities_ignore_0_axis=[], activities_ignore_1_axis=[]
    )

    # two weeks represantative of 14 days
    for day_i in range(14):
        if day_i == 1:
            int_mat[DiscordActivity.Reaction][0, 1] = 0
            int_mat[DiscordActivity.Reaction][1, 0] = 0

        if day_i == 3:
            int_mat[DiscordActivity.Reaction][2, 3] = 2
            int_mat[DiscordActivity.Reaction][3, 2] = 4

        if day_i == 4:
            int_mat[DiscordActivity.Reaction][2, 3] = 0
            int_mat[DiscordActivity.Reaction][3, 2] = 0

        (_, *computed_activities) = engagement.compute(
            int_mat=int_mat,
            w_i=day_i,
            acc_names=acc_names,
            act_param=act_param,
            WINDOW_D=WINDOW_D,
            **activity_dict
        )

        computed_activities = dict(zip(activity_dict.keys(), computed_activities))
        activity_dict = computed_activities
    print(activity_dict["all_active"])

    assert activity_dict["all_active"] == {
        "0": {"user1", "user0"},
        "1": set(),
        "2": set(),
        "3": {"user2", "user3"},
        "4": set(),
        "5": set(),
        "6": set(),
        "7": set(),
        "8": set(),
        "9": set(),
        "10": set(),
        "11": set(),
        "12": set(),
        "13": set(),
    }
