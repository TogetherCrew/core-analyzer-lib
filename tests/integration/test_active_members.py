import numpy as np
from analyzer.assess_engagement import EngagementAssessment
from analyzer.utils.activity import DiscordActivity


def test_no_active():
    acc_names = []
    acc_count = 5
    for i in range(5):
        acc_names.append(f"user{i}")

    acc_names = np.array(acc_names)

    int_mat = {
        DiscordActivity.Reply: np.zeros((acc_count, acc_count)),
        DiscordActivity.Mention: np.zeros((acc_count, acc_count)),
        DiscordActivity.Reaction: np.zeros((acc_count, acc_count)),
    }

    activity_dict = {
        "all_joined": {},
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

    WINDOW_D = 7

    # window index
    w_i = 0

    INT_THR = 1  # minimum number of interactions to be active
    UW_DEG_THR = 1  # minimum number of accounts interacted with to be active
    PAUSED_T_THR = 1  # time period to remain paused
    CON_T_THR = 4  # time period to be consistent active
    CON_O_THR = 3  # time period to be consistent active
    EDGE_STR_THR = 5  # minimum number of interactions for connected
    UW_THR_DEG_THR = 5  # minimum number of accounts for connected
    VITAL_T_THR = 4  # time period to assess for vital
    VITAL_O_THR = 3  # times to be connected within VITAL_T_THR to be vital
    STILL_T_THR = 2  # time period to assess for still active
    STILL_O_THR = 2  # times to be active within STILL_T_THR to be still active

    # time periods into the past (history) to be newly active for computing dropped
    DROP_H_THR = 2

    # consecutive time periods into the past to have not been active for computing
    DROP_I_THR = 1

    act_param = [
        INT_THR,
        UW_DEG_THR,
        PAUSED_T_THR,
        CON_T_THR,
        CON_O_THR,
        EDGE_STR_THR,
        UW_THR_DEG_THR,
        VITAL_T_THR,
        VITAL_O_THR,
        STILL_T_THR,
        STILL_O_THR,
        DROP_H_THR,
        DROP_I_THR,
    ]

    activities = [
        DiscordActivity.Reaction,
        DiscordActivity.Mention,
        DiscordActivity.Reply,
    ]

    engagement = EngagementAssessment(
        activities=activities, activities_ignore_0_axis=[], activities_ignore_1_axis=[]
    )

    (_, *computed_activities) = engagement.compute(
        int_mat=int_mat,
        w_i=w_i,
        acc_names=acc_names,
        act_param=act_param,
        WINDOW_D=WINDOW_D,
        **activity_dict,
    )

    computed_activities = dict(zip(activity_dict.keys(), computed_activities))

    assert computed_activities["all_joined"] == {}
    assert computed_activities["all_joined_day"] == {"0": set()}
    assert computed_activities["all_consistent"] == {"0": set()}
    assert computed_activities["all_vital"] == {"0": set()}
    assert computed_activities["all_active"] == {"0": set()}
    assert computed_activities["all_connected"] == {"0": set()}
    assert computed_activities["all_dropped"] == {"0": set()}
    assert computed_activities["all_new_active"] == {"0": set()}
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


def test_single_active():
    acc_names = []
    acc_count = 5
    for i in range(5):
        acc_names.append(f"user{i}")

    acc_names = np.array(acc_names)

    int_mat = {
        DiscordActivity.Reply: np.zeros((acc_count, acc_count)),
        DiscordActivity.Mention: np.zeros((acc_count, acc_count)),
        DiscordActivity.Reaction: np.zeros((acc_count, acc_count)),
    }
    int_mat[DiscordActivity.Reply][0, 1] = 2

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
    # time window
    WINDOW_D = 7
    # window index
    w_i = 0

    INT_THR = 1  # minimum number of interactions to be active
    UW_DEG_THR = 1  # minimum number of accounts interacted with to be active
    PAUSED_T_THR = 1  # time period to remain paused
    CON_T_THR = 4  # time period to be consistent active
    CON_O_THR = 3  # time period to be consistent active
    EDGE_STR_THR = 5  # minimum number of interactions for connected
    UW_THR_DEG_THR = 5  # minimum number of accounts for connected
    VITAL_T_THR = 4  # time period to assess for vital
    VITAL_O_THR = 3  # times to be connected within VITAL_T_THR to be vital
    STILL_T_THR = 2  # time period to assess for still active
    STILL_O_THR = 2  # times to be active within STILL_T_THR to be still active
    # time periods into the past (history) to be newly active for computing dropped
    DROP_H_THR = 2
    # consecutive time periods into the past to have not been active for computing
    DROP_I_THR = 1

    act_param = [
        INT_THR,
        UW_DEG_THR,
        PAUSED_T_THR,
        CON_T_THR,
        CON_O_THR,
        EDGE_STR_THR,
        UW_THR_DEG_THR,
        VITAL_T_THR,
        VITAL_O_THR,
        STILL_T_THR,
        STILL_O_THR,
        DROP_H_THR,
        DROP_I_THR,
    ]

    activities = [
        DiscordActivity.Reaction,
        DiscordActivity.Mention,
        DiscordActivity.Reply,
    ]

    engagement = EngagementAssessment(
        activities=activities, activities_ignore_0_axis=[], activities_ignore_1_axis=[]
    )

    (_, *computed_activities) = engagement.compute(
        int_mat=int_mat,
        w_i=w_i,
        acc_names=acc_names,
        act_param=act_param,
        WINDOW_D=WINDOW_D,
        **activity_dict,
    )

    computed_activities = dict(zip(activity_dict.keys(), computed_activities))

    assert computed_activities["all_joined"] == {"0": set()}
    assert computed_activities["all_consistent"] == {"0": set()}
    assert computed_activities["all_vital"] == {"0": set()}
    assert computed_activities["all_active"] == {"0": set(["user0", "user1"])}
    assert computed_activities["all_connected"] == {"0": set()}
    assert computed_activities["all_dropped"] == {"0": set()}
    assert computed_activities["all_new_active"] == {"0": set(["user0", "user1"])}
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
