from analyzer.utils.assessments import assess_vital


def test_assess_vital():
    """
    test the assess_vital module
    """
    all_connected = {
        "0": set(["user0", "user1", "user2", "user3", "user4"]),
    }
    all_vital: dict[str, set[str]] = {
        "0": set(),
    }

    # For testing purposes we're setting 1 for each parameters of vital
    all_vital = assess_vital(
        all_connected=all_connected,
        w_i=1,
        VITAL_T_THR=1,  # 1 time to be considered as vital
        VITAL_O_THR=1,  # 1 time occured to be consired as vital
        WINDOW_D=1,
        all_vital=all_vital,
    )

    assert all_vital["1"] == set(["user0", "user1", "user2", "user3", "user4"])
