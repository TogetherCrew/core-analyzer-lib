def assess_overlap(
    ref_dict: dict[str, set[str]],
    comp_dict: dict[str, set[str]],
    w_i: int,
    num_past: int,
) -> tuple[set[str], set[str]]:
    w_i_str = str(w_i)

    # define comparison period
    comp_per = int(w_i_str) - num_past

    # if comparison period is present in keys
    if str(comp_per) in comp_dict.keys():
        # assess overlap
        overlap_acc = set(ref_dict[w_i_str]).intersection(set(comp_dict[str(comp_per)]))

        # store remaining accounts
        rem_acc = set(ref_dict[w_i_str]) - overlap_acc

    else:
        # store empty set
        overlap_acc = set("")

        # set remaining accounts to all initial accounts
        rem_acc = set(ref_dict[w_i_str])

    return (rem_acc, overlap_acc)
