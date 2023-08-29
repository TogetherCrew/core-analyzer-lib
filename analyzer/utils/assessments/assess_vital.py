from .check_past import check_past


def assess_vital(
    all_connected: dict[str, set[str]],
    w_i: int,
    VITAL_T_THR: int,
    VITAL_O_THR: int,
    WINDOW_D: int,
    all_vital: dict[str, set[str]],
) -> dict[str, set[str]]:
    """
    Assess all vital accounts

    Parameters:
    ------------
    all_connected : dict[str, set[str]]
        dictionary with keys w_i and values
        containing a list of all account names that are connected
    w_i : int
        index of sliding time window
    VITAL_T_THR : int
        time period to assess for vital
    VITAL_O_THR : int
        times to be connected within VITAL_T_THR to be vital
    WINDOW_D : int
        duration of sliding window (days)
    all_vital : dict[str, set[str]]
        dictionary with keys w_i and values
        containing a list of all account names that are vital

    Returns:
    ----------
    all_vital : dict[str, set[str]]
        dictionary with keys w_i and values
        containing a list of all account names that are vital updated
        for window w_i
    """

    # if there are more time periods in the past than CON_T_THR
    # checking non-verlapping periods
    if w_i - VITAL_O_THR * WINDOW_D >= 0:
        # obtain who was connected in all specified time periods and was engaged
        all_vital[str(w_i)] = set(
            check_past(all_connected, VITAL_T_THR, VITAL_O_THR, WINDOW_D)
        )

    else:
        # store empty set
        all_vital[str(w_i)] = set("")

    return all_vital
