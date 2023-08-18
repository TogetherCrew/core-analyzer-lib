from .check_past import check_past
from .check_prev_period import check_prev_period


def assess_remainder(
    all_active: dict[str, set[str]],
    w_i: int,
    WINDOW_D: int,
    PAUSED_T_THR: int,
    all_new_active: dict[str, set[str]],
    all_unpaused: dict[str, set[str]],
    all_returned: dict[str, set[str]],
    all_paused: dict[str, set[str]],
    all_new_disengaged: dict[str, set[str]],
    all_disengaged: dict[str, set[str]],
    all_disengaged_in_past: dict[str, set[str]],
) -> tuple[
    dict[str, set[str]],
    dict[str, set[str]],
    dict[str, set[str]],
    dict[str, set[str]],
    dict[str, set[str]],
    dict[str, set[str]],
    dict[str, set[str]],
]:
    """
    Assess all remaing engagement categories

    Parameters:
    -------------
    all_active : dict[str, set[str]]
        dictionary with keys w_i and values
        containing a list of all account names that are active
    w_i : int
        index of sliding time window
    WINDOW_D : int
        duration of sliding window (days)
    PAUSED_T_THR : int
        time period to remain paused
    all_* : dict[str, set[str]]
        dictionary with keys w_i and values
        containing a list of all account names that are *

    Returns:
    ----------
    all_new_active : dict[str, set[str]]
        dictionary with keys w_i and values
        containing a list of all account names that are new_active updated
        for window w_i
    all_unpaused : dict[str, set[str]]
        dictionary with keys w_i and values
        containing a list of all account names that are unpaused updated
        for window w_i
    all_returned : dict[str, set[str]]
        dictionary with keys w_i and values
        containing a list of all account names that are returned updated
        for window w_i
    all_paused : dict[str, set[str]]
        dictionary with keys w_i and values
        containing a list of all account names that are paused updated
        for window w_i
    all_new_disengaged : dict[str, set[str]]
        dictionary with keys w_i and values
        containing a list of all account names that are newly disengaged updated
        for window w_i
    all_disengaged : dict[str, set[str]]
        dictionary with keys w_i and values
        containing a list of all account names that are disengaged updated
        for window w_i
    all_disengaged_in_past : dict[str, set[str]]
        dictionary with keys w_i and values
        containing a list of all account names that are disengaged in past updated
        for window w_i
    """

    # if data from previous period is available
    if (w_i - WINDOW_D >= 0) and (str(w_i - WINDOW_D) in all_active.keys()):
        # check if there is paused data from previous period
        #  and otherwise make empty set
        temp_set_paused = check_prev_period(all_paused, str(w_i - WINDOW_D))

        # check if there is disengaged data from
        #  previous period and otherwise make empty set
        temp_set_disengaged = check_prev_period(all_disengaged, str(w_i - WINDOW_D))

        # check if there is unpaused data from previous period and
        #  otherwise make empty set
        temp_set_unpaused = check_prev_period(all_unpaused, str(w_i - WINDOW_D))

        # # # NEWLY ACTIVE # # #

        # obtain members active in this window that were not active,
        #  paused or disengaged WINDOW_D days ago
        all_new_active[str(w_i)] = (
            set(all_active[str(w_i)])
            - set(all_active[str(w_i - WINDOW_D)])
            - temp_set_paused
            - temp_set_disengaged
            - temp_set_unpaused
        )

        # # # PAUSED (1 of 2)# # #

        # obtain members that were active WINDOW_D days ago
        #  but are not active in this window
        new_paused = set(all_active[str(w_i - WINDOW_D)]) - set(all_active[str(w_i)])

        # add newly paused members to paused members from previous period
        temp_currently_paused = new_paused.union(temp_set_paused)

        # create temporary empty set result (will be updated in part 2 of 2)
        all_paused[str(w_i)] = set("")

        # if data from previous previous period is available
        if w_i - 2 * WINDOW_D >= 0:
            # # # UNPAUSED # # #

            # obtain account names active now but paused WINDOW_D days ago
            all_unpaused[str(w_i)] = set(all_paused[str(w_i - WINDOW_D)]).intersection(
                all_active[str(w_i)]
            )

            # remove unpaused from currently paused
            temp_currently_paused = temp_currently_paused - all_unpaused[str(w_i)]

            # # # RETURNED # # #

            # if there is disengaged data for this time period
            if str(w_i - WINDOW_D) in all_disengaged.keys():
                # obtain account names active now but disengaged WINDOW_D days ago
                all_returned[str(w_i)] = set(
                    all_disengaged[str(w_i - WINDOW_D)]
                ).intersection(all_active[str(w_i)])

            else:
                # store empty set for returned
                all_returned[str(w_i)] = set("")

            # # # DISENGAGED # # #

            # obtain account names that were continuously
            #  paused for PAUSED_T_THR periods
            cont_paused = check_past(
                all_paused, PAUSED_T_THR + 1, PAUSED_T_THR, WINDOW_D
            )

            # obtain account names that were
            #  continuously paused and are still not active
            all_new_disengaged[str(w_i)] = set(
                cont_paused.intersection(temp_currently_paused)
            )

            # add newly disengaged members to disengaged members
            #  from previous period
            temp_currently_disengaged = all_new_disengaged[str(w_i)].union(
                temp_set_disengaged
            )

            # remove returned accounts from disengaged accounts and store
            all_disengaged[str(w_i)] = set(
                temp_currently_disengaged - all_returned[str(w_i)]
            )

            # store who disengaged in the past
            all_disengaged_in_past[str(w_i)] = (
                all_disengaged[str(w_i)] - all_new_disengaged[str(w_i)]
            )

            # remove disengaged accounts from paused accounts
            temp_currently_paused = temp_currently_paused - all_disengaged[str(w_i)]

        else:
            all_disengaged[str(w_i)] = set([])
            all_new_disengaged[str(w_i)] = set([])
            all_unpaused[str(w_i)] = set([])
            all_returned[str(w_i)] = set([])
            all_disengaged_in_past[str(w_i)] = set([])

        # # # PAUSED (2 of 2) # # #

        # store currently paused accounts
        all_paused[str(w_i)] = set(temp_currently_paused)

    else:
        # set all active members to newly active
        all_new_active[str(w_i)] = set(all_active[str(w_i)])

        # set remaining activity types to empty string
        all_paused[str(w_i)] = set("")
        all_unpaused[str(w_i)] = set("")
        all_returned[str(w_i)] = set("")
        all_new_disengaged[str(w_i)] = set("")
        all_disengaged[str(w_i)] = set("")
        all_disengaged_in_past[str(w_i)] = set("")

    return (
        all_new_active,
        all_unpaused,
        all_returned,
        all_paused,
        all_new_disengaged,
        all_disengaged,
        all_disengaged_in_past,
    )
