from tc_core_analyzer_lib.utils.assessments.check_prev_period import check_prev_period


def test_available_previous_data():
    """
    test the module in case of that data being available
    """

    data: dict[str, set[str]] = {"0": set(["user0", "user2", "user3"])}

    results = check_prev_period(engagement_dict=data, time_str="0")

    assert results == set(["user0", "user2", "user3"])


def test_no_previous_data():
    """
    test the module in case of that data being available
    """

    data: dict[str, set[str]] = {}

    results = check_prev_period(engagement_dict=data, time_str="0")

    assert results == set([])
