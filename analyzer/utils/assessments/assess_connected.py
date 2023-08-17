import numpy as np


def assess_connected(
    acc_names: np.ndarray,
    thr_uw_thr_deg: list[int],
    w_i: int,
    all_connected: dict[str, set[str]],
) -> dict[str, set[str]]:
    """
    Assess all connected accounts

    Parameters:
    ------------
    acc_names : np.ndarray[str]
        all active accounts in window
        the account names are string
    thr_uw_thr_deg : list[int]
        index numbers of account names with at
        least `UW_THR_DEG_THR` connections of at least `EDGE_STR_THR`
        interactions each
    w_i : list[int]
        index of sliding time window
    all_connected : dict[str, set[str]]
        dictionary with keys w_i and values
        containing a list of all account names that are connected

    Returns:
    -----------
    all_connected - dict[str, set[str]]
        dictionary with keys w_i and values
        containing a list of all account names that are connected updated
        for window w_i
    """

    # obtain connected account names in this period and store in dictionary
    all_connected[str(w_i)] = set(acc_names[thr_uw_thr_deg])

    return all_connected
