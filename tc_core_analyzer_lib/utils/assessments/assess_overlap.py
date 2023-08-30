def assess_overlap(
    ref_dict: dict[str, set[str]],
    comp_dict: dict[str, set[str]],
    w_i: int,
    num_past: int,
) -> tuple[set[str], set[str]]:
    """
    Assesses the overlap between member type dictionaries at selected time points
    Notes: The comparison set needs to be at the same time point (num_past = 0)
    or a previous time point (num_past > 0) relative to reference set.
    If a future time point is required, switch ref_dict and comp_dict

    Parameters:
    ------------
    ref_dict : dict[str, set[str]]
        reference dictionary to be used in the comparison
    comp_dict : dict[str, set[str]]
        comparison dictionary to be used in the comparison.
    w_i : int
        time period for set from ref_dict
    num_past : int
        number of time periods previous to w_i for set from comp_dict

    Returns:
    ---------
    rem_acc : set[str]
        remaining accounts from ref_dict[w_i]
        that do not overlap with the selected comp_dict set
    overlap_acc : set[str]
        accounts that overlap between ref_dict[w_i]
        and the selected comp_dict set
    """
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
