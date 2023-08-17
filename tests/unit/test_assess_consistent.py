from analyzer.utils.assessments import assess_consistent


def test_assess_vital():
    """
    test the assess_vital module
    """
    all_active = {
        "0": set(["user0", "user1", "user2", "user3", "user4"]),
    }
    all_consistent: dict[str, set[str]] = {
        "0": set(),
    }

    # For testing purposes we're setting 1 for each parameters of vital
    all_consistent = assess_consistent(
        all_active=all_active,
        w_i=1,
        CON_O_THR=1,  # 1 time to be considered as vital
        CON_T_THR=1,  # 1 time occured to be consired as vital
        WINDOW_D=7,
        all_consistent=all_consistent,
    )

    assert all_consistent["1"] == set(["user0", "user1", "user2", "user3", "user4"])
