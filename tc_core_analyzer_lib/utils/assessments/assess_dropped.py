from .check_past import check_past


def assess_dropped(
    all_new_active: dict[str, set[str]],
    all_active: dict[str, set[str]],
    w_i: int,
    DROP_H_THR: int,
    DROP_I_THR: int,
    WINDOW_D: int,
    all_dropped: dict[str, set[str]],
) -> dict[str, set[str]]:
    """
    Assess all dropped accounts

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
    DROP_H_THR : int
        time periods in the past to have been newly active
    DROP_I_THR : int
        time periods to have been inactive
    WINDOW_D : int
        duration of sliding window (days)
    all_dropped : dict[str, set[str]]
        dictionary with keys w_i and values
        containing a list of all account names that are dropped

    Returns:
    ----------
    all_dropped : dict[str, set[str]]
        dictionary with keys w_i and values
        containing a list of all account names that are dropped
        updated for window w_i
    """

    # if there are more time periods in the past than STILL_T_THR
    if w_i - (DROP_H_THR * WINDOW_D) >= 0:
        # obtain who was newly active in one of specified time periods
        all_new_per = set(check_past(all_new_active, DROP_H_THR, 1, WINDOW_D))

        # obtain who was active in one of the specified time periods
        all_act_per = set(check_past(all_active, DROP_I_THR, 1, WINDOW_D))

        # remove all_act_per from all_new_per and store results
        all_dropped[str(w_i)] = set(all_new_per - all_act_per)

    else:
        # store empty set
        all_dropped[str(w_i)] = set("")

    return all_dropped
