from tc_core_analyzer_lib.utils.assessments.check_past import check_past


def test_check_past_two_day_periods():
    """
    test check past with each period as 2 days
    so the values like `0, 1` and `1, 2`, etc would be overlapping periods
    """
    # each period is 2 days
    WINDOW_D = 2

    data_dict = {
        "0": set(["user0", "user1", "user2", "user3", "user4"]),
        "1": set(["user0", "user1", "user2", "user3"]),
        "2": set(["user0", "user1", "user2", "user3"]),
        "3": set(["user1", "user2"]),
        "4": set(["user1", "user3"]),
        "5": set(["user0", "user1", "user2", "user3"]),
        "6": set(["user0", "user1", "user2", "user3", "user4"]),
        "7": set(["user0", "user1", "user2", "user3", "user4"]),
    }

    data = check_past(data_dic=data_dict, t_thr=2, o_thr=2, WINDOW_D=WINDOW_D)

    assert data == set(["user0", "user1", "user2", "user3"])
