from .check_past import check_past


def assess_consistent(
    all_active: dict[str, set[str]],
    w_i: int,
    CON_T_THR: int,
    CON_O_THR: int,
    WINDOW_D: int,
    all_consistent: dict[str, set[str]],
) -> dict[str, set[str]]:
    """
    Assess all continuously active accounts

    Parameters:
    -------------
    all_active : dict[str, set[str]]
        dictionary with keys w_i and values
        containing a list of all account names that are active
    w_i : int
        index of sliding time window
    CON_T_THR : int
        time period to assess consistently active
    CON_O_THR : int
        times to be active within `CON_T_THR` to be
        consistently active
    WINDOW_D : int
        duration of sliding window (days)
    n_consistent : list[int]
        list of number of accounts that are continuously active
    all_consistent : dict[str, set[str]]
        dictionary with keys w_i and values
        containing a list of all account names that are continuously active

    Returns:
    ---------
    all_consistent : dict[str, set[str]]
        dictionary with keys w_i and values
        containing a list of all account names that are consistently active updated
        for window w_i
    """

    # if there are more time periods in the past than CON_O_THR
    if w_i - (CON_O_THR - 1) * WINDOW_D >= 0:
        # obtain who was consistently active in all specified time periods
        all_consistent[str(w_i)] = set(
            check_past(all_active, CON_T_THR, CON_O_THR, WINDOW_D)
        )

    else:
        # store empty set
        all_consistent[str(w_i)] = set("")

    return all_consistent
