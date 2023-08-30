from .check_past import check_past


def assess_still_active(
    all_new_active: dict[str, set[str]],
    all_active: dict[str, set[str]],
    w_i: int,
    STILL_T_THR: int,
    STILL_O_THR: int,
    WINDOW_D: int,
    all_still_active: dict[str, set[str]],
) -> dict[str, set[str]]:
    """
    Assess all still active accounts

    Parameters:
    -------------
    all_new_active : dict[str, set[str]]
        dictionary with keys w_i and values
        containing a list of all account names that are active for first
         time in period
    all_active : dict[str, set[str]]
        dictionary with keys w_i and values
        containing a list of all account names that are active
    w_i : int
        index of sliding time window
    STILL_T_THR : int
        time period to assess for still active
    STILL_O_THR : int
        times to be active within STILL_T_THR to be still active
    WINDOW_D : int
        duration of sliding window (days)
    all_still_active : dict[str, set[str]]
        dictionary with keys w_i and values
        containing a list of all account names that are still active

    Returns:
    ----------
    all_still_active : dict[str, set[str]]
        dictionary with keys w_i and values
        containing a list of all account names that are still active
        updated for window w_i
    """

    # if there are more time periods in the past than STILL_T_THR
    if w_i - (STILL_T_THR * WINDOW_D) >= 0:
        # obtain who was active in sufficient specified time periods
        all_con_active = set(check_past(all_active, STILL_T_THR, STILL_O_THR, WINDOW_D))

        # select who of all_con_active were part of all arrived in period and store
        all_still_active[str(w_i)] = set(
            all_con_active.intersection(
                all_new_active[str(w_i - (STILL_T_THR * WINDOW_D))]
            )
        )

    else:
        # store empty set
        all_still_active[str(w_i)] = set("")

    return all_still_active
