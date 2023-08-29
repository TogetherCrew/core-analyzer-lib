import numpy as np
from tc_core_analyzer_lib.assess_engagement import assess_active


def test_assess_active():
    acc_names = np.array(["user0", "user1", "user2", "user3", "user4", "user5"])

    all_active: dict[str, set[str]] = {}
    all_active = assess_active(
        acc_names=acc_names,
        thr_ind=[0, 1, 4, 5],
        thr_uw_deg=[1, 3, 4, 5],
        w_i=0,
        all_active=all_active,
    )

    assert all_active["0"] == set(["user1", "user4", "user5"])
