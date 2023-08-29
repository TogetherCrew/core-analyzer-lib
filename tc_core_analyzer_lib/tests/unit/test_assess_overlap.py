from tc_core_analyzer_lib.utils.assessments.assess_overlap import assess_overlap


def test_assess_overlap():
    reference_dict: dict[str, set[str]] = {
        "0": set(["user0", "user2", "user4"]),
        "1": set(["user1", "user2", "user3", "user5"]),
        "2": set(["user0", "user3", "user4"]),
    }
    comparison_dict: dict[str, set[str]] = {
        "0": set(["user0", "user1", "user5"]),
        "1": set(["user1", "user3", "user4"]),
        "2": set(["user0", "user1", "user3", "user4", "user5"]),
    }

    results_overlapping = []
    results_remainder = []

    for w_i in reference_dict.keys():
        rem_acc, overlap_acc = assess_overlap(
            ref_dict=reference_dict, comp_dict=comparison_dict, w_i=int(w_i), num_past=0
        )

        results_overlapping.append(overlap_acc)
        results_remainder.append(rem_acc)

    assert results_overlapping == [
        set(["user0"]),
        set(["user1", "user3"]),
        set(["user0", "user3", "user4"]),
    ]

    assert results_remainder == [
        set(["user2", "user4"]),
        set(["user2", "user5"]),
        set([]),
    ]
