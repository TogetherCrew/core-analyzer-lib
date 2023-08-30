from tc_core_analyzer_lib.utils.assessments import assess_vital


def test_assess_vital_continuos():
    """
    test the assess_vital module in contnuos periods
    """
    all_connected = {
        "0": set(["user0", "user1", "user2", "user3", "user4"]),
        "1": set(["user0", "user1", "user2", "user3", "user4"]),
        "2": set(["user0", "user1", "user2", "user3", "user4"]),
        "3": set([]),
    }
    all_vital: dict[str, set[str]] = {
        "0": set(),
        "1": set(),
        "2": set(),
        "3": set(),
    }

    all_vital = assess_vital(
        all_connected=all_connected,
        w_i=4,
        VITAL_T_THR=4,  # 4 time to be considered as vital
        VITAL_O_THR=3,  # 3 time occured to be consired as vital
        WINDOW_D=1,
        all_vital=all_vital,
    )

    assert all_vital["4"] == set(["user0", "user1", "user2", "user3", "user4"])


def test_assess_vital_different_periods():
    """
    test the assess_vital module in different periods
    """
    all_connected = {
        "0": set(["user0", "user1", "user2", "user3", "user4"]),
        "1": set(["user0", "user1", "user2", "user3", "user4"]),
        "2": set([]),
        "3": set(["user0", "user1", "user2", "user3", "user4"]),
    }
    all_vital: dict[str, set[str]] = {
        "0": set(),
        "1": set(),
        "2": set(),
        "3": set(),
    }

    # For testing purposes we're setting 1 for each parameters of vital
    all_vital = assess_vital(
        all_connected=all_connected,
        w_i=4,
        VITAL_T_THR=4,  # 1 time to be considered as vital
        VITAL_O_THR=3,  # 1 time occured to be consired as vital
        WINDOW_D=1,
        all_vital=all_vital,
    )

    assert all_vital["4"] == set(["user0", "user1", "user2", "user3", "user4"])


def test_assess_vital_different_periods_not_first():
    """
    test the assess_vital module in different periods
    """
    all_connected = {
        "0": set([]),
        "1": set(["user0", "user1", "user2", "user3", "user4"]),
        "2": set(["user0", "user1", "user2", "user3", "user4"]),
        "3": set(["user0", "user1", "user2", "user3", "user4"]),
    }
    all_vital: dict[str, set[str]] = {
        "0": set(),
        "1": set(),
        "2": set(),
        "3": set(),
    }

    # For testing purposes we're setting 1 for each parameters of vital
    all_vital = assess_vital(
        all_connected=all_connected,
        w_i=4,
        VITAL_T_THR=4,  # 1 time to be considered as vital
        VITAL_O_THR=3,  # 1 time occured to be consired as vital
        WINDOW_D=1,
        all_vital=all_vital,
    )

    assert all_vital["4"] == set(["user0", "user1", "user2", "user3", "user4"])
