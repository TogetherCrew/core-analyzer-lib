from tc_core_analyzer_lib.utils.assessments.assess_remainder import assess_remainder


def test_assess_paused():
    all_active = {
        "0": set(["user0", "user1", "user2", "user3", "user4"]),
        "1": set(["user0", "user1", "user2", "user3", "user5"]),
    }

    all_new_active = {"0": set(["user0", "user1", "user2", "user3", "user4"])}
    all_unpaused = {"0": set([])}
    all_returned = {"0": set([])}
    all_paused = {"0": set([])}
    all_disengaged = {"0": set([])}
    all_disengaged_in_past = {"0": set([])}
    all_new_disengaged = {"0": set([])}

    (
        all_new_active,
        all_unpaused,
        all_returned,
        all_paused,
        all_new_disengaged,
        all_disengaged,
        all_disengaged_in_past,
    ) = assess_remainder(
        all_active=all_active,
        w_i=1,
        WINDOW_D=1,
        PAUSED_T_THR=1,
        all_new_active=all_new_active,
        all_unpaused=all_unpaused,
        all_returned=all_returned,
        all_paused=all_paused,
        all_disengaged=all_disengaged,
        all_disengaged_in_past=all_disengaged_in_past,
        all_new_disengaged=all_new_disengaged,
    )

    assert all_paused["1"] == set(["user4"])
    assert all_unpaused["1"] == set([])
    assert all_returned["1"] == set([])
    assert all_new_disengaged["1"] == set([])
    assert all_disengaged_in_past["1"] == set([])
