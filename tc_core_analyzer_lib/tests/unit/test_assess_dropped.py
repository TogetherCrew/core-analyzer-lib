from tc_core_analyzer_lib.utils.assessments.assess_dropped import assess_dropped


def test_all_dropped():
    all_new_active: dict[str, set[str]] = {
        "0": set(["user0", "user2", "user4"]),
        "1": set(["user1", "user3", "user5"]),
        "2": set(["user6", "user7"]),
    }
    all_active: dict[str, set[str]] = {
        "0": set(["user0", "user2", "user4"]),
        "1": set(["user1", "user2", "user3", "user4", "user5"]),
        "2": set(["user6", "user3", "user4", "user7"]),
    }
    all_dropped: dict[str, set[str]] = {
        "0": set([]),
        "1": set([]),
    }

    all_dropped = assess_dropped(
        all_new_active=all_new_active,
        all_active=all_active,
        w_i=2,
        DROP_H_THR=2,
        DROP_I_THR=1,
        WINDOW_D=1,
        all_dropped=all_dropped,
    )

    assert all_dropped == {
        "0": set([]),
        "1": set([]),
        "2": set(["user1", "user5"]),
    }
