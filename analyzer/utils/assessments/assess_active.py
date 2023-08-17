from numpy import intersect1d, ndarray


def assess_active(
    acc_names: ndarray,
    thr_ind: list[str],
    thr_uw_deg: list[str],
    w_i: int,
    all_active: dict[str, set[str]],
) -> dict[str, set[str]]:
    """
    Assess all active accounts

    Parameters:
    -------------
    acc_names : np.ndarray[str]
        all active accounts in window
    thr_ind : list[int]
        index numbers of account names with at least
        `INT_THR` interactions in which the `INT_THR` is an integer positive value
    thr_uw_deg : list[int]
        index numbers of account names with at least
        `UW_DEG_THR` connections in which the `UW_DEG_THR` is
        an integer positive value
    w_i : int
        index of the sliding time window
        which is an integer value
    all_active : dict[str, set[str]]
        dictionary with string keys of `w_i` and values
        containing a list of all account names that are active

    Returns:
    ---------
    all_active - dict[str, set[str]] : dictionary with keys w_i and values
        containing a list of all account names that are active updated
        for window `w_i`
    """

    # obtain accounts that meet both weigthed and unweighted degree thresholds
    thr_overlap = intersect1d(thr_ind, thr_uw_deg)

    # obtain active account names in this period and store in dictionary
    all_active[str(w_i)] = set(acc_names[thr_overlap])

    return all_active
