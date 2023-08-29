from tc_core_analyzer_lib.utils.assessments.assess_still_active import (
    assess_still_active,
)


def test_still_active():
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
    all_still_active: dict[str, set[str]] = {
        "0": set([]),
        "1": set([]),
    }

    all_still_active = assess_still_active(
        all_new_active=all_new_active,
        all_active=all_active,
        w_i=2,
        STILL_O_THR=2,
        STILL_T_THR=2,
        WINDOW_D=1,
        all_still_active=all_still_active,
    )

    assert all_still_active == {
        "0": set([]),
        "1": set([]),
        "2": set(["user4"]),
    }
