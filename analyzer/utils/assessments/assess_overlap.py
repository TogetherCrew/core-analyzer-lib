def assess_overlap(
    ref_dict: dict[str, set[str]],
    comp_dict: dict[str, set[str]],
    w_i: int,
    num_past: int,
) -> tuple[dict[str, set[str]], dict[str, set[str]]]:
    # define comparison period
    comp_per = int(w_i) - num_past

    # if comparison period is present in keys
    if str(comp_per) in comp_dict.keys():
        # assess overlap
        overlap_acc = set(ref_dict[w_i]).intersection(set(comp_dict[str(comp_per)]))

        # store remaining accounts
        rem_acc = set(ref_dict[w_i]) - overlap_acc

    else:
        # store empty set
        overlap_acc = set("")

        # set remaining accounts to all initial accounts
        rem_acc = set(ref_dict[w_i])

    return [rem_acc, overlap_acc]
