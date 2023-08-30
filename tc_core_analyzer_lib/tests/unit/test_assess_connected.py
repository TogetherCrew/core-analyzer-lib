import numpy as np
from tc_core_analyzer_lib.assess_engagement import assess_connected


def test_assess_connected():
    acc_names = np.array(["user0", "user1", "user2", "user3", "user4", "user5"])

    all_connected: dict[str, set[str]] = {}
    all_connected = assess_connected(
        acc_names=acc_names,
        thr_uw_thr_deg=[0, 2, 4],
        w_i=0,
        all_connected=all_connected,
    )

    assert all_connected["0"] == set(["user0", "user2", "user4"])
