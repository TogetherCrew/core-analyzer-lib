from tc_core_analyzer_lib.utils.assessments import assess_lurker


def test_assess_lurker():
    """
    test the assess_vital module
    """
    all_new_active = {
        "0": set(["user0", "user1", "user2", "user3", "user4"]),
        "1": set(["user1", "user2", "user3", "user4"]),
    }
    all_lurker = {"0": set()}

    all_joined_day: dict[str, set[str]] = {
        "0": set(),
        "1": set(["user2", "user3", "user4", "user5", "user6"]),
    }

    # For testing purposes we're setting 1 for each parameters of vital
    all_lurker = assess_lurker(
        all_lurker=all_lurker,
        all_new_active=all_new_active,
        all_joined_day=all_joined_day,
        w_i=1,
    )

    assert all_lurker["1"] == set(["user5", "user6"])
