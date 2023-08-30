from tc_core_analyzer_lib.utils.assessments import assess_consistent


def test_assess_consistent_continuos():
    """
    test the assess_consistent module
    """
    all_active = {
        "0": set(["user0", "user1", "user2", "user3", "user4"]),
        "1": set(["user0", "user1", "user2", "user3", "user4"]),
        "2": set([]),
    }
    all_consistent: dict[str, set[str]] = {
        "0": set(),
        "1": set(),
        "2": set(),
    }

    # For testing purposes we're setting 1 for each parameters of consistent
    all_consistent = assess_consistent(
        all_active=all_active,
        w_i=3,
        CON_O_THR=2,  # 1 time to be considered as consistent
        CON_T_THR=3,  # 1 time occured to be consired as consistent
        WINDOW_D=1,
        all_consistent=all_consistent,
    )

    assert all_consistent["3"] == set(["user0", "user1", "user2", "user3", "user4"])


def test_assess_consistent_different_periods():
    """
    test the assess_consistent module with not continuos periods
    """
    all_active = {
        "0": set(["user0", "user1", "user2", "user3", "user4"]),
        "1": set([]),
        "2": set(["user0", "user1", "user2", "user3", "user4"]),
    }
    all_consistent: dict[str, set[str]] = {
        "0": set(),
        "1": set(),
        "2": set(),
    }

    # For testing purposes we're setting 1 for each parameters of consistent
    all_consistent = assess_consistent(
        all_active=all_active,
        w_i=3,
        CON_O_THR=2,  # 1 time to be considered as consistent
        CON_T_THR=3,  # 1 time occured to be consired as consistent
        WINDOW_D=1,
        all_consistent=all_consistent,
    )

    assert all_consistent["3"] == set(["user0", "user1", "user2", "user3", "user4"])
