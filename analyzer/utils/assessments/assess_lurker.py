def assess_lurker(
    all_lurker: dict[str, set[str]],
    all_new_active: dict[str, set[str]],
    all_joined_day: dict[str, set[str]],
    w_i: int,
):
    """
    Assess all lurker accounts

    Parameters:
    ------------
    all_lurker : dict[str, set[str]]
        dictionary with keys w_i and values
        containing a list of all account names that are lurkers
    all_new_active : dict[str, set[str]]
        dictionary with keys w_i and values
        containing a list of all account names that are active for first
         time in period
    all_joined_day : dict[str, set[str]]
        dictionary with keys w_i and values
        containing a list of all account names that joined on w_i
    w_i : int
        index of sliding time window

    Returns:
    ---------
    all_lurker : dict[str, set[str]]
        dictionary with keys w_i and values
        containing a list of all account names that are lurkers
        updated for window w_i
    """
    # if data for previous period exists
    if w_i >= 1:
        # combine lurker from previous period with newly joined from this period
        temp_lurker = set(all_lurker[str(w_i - 1)]).union(set(all_joined_day[str(w_i)]))

    # if this is the first period
    else:
        # store all joined accounts as temp_lurkers
        data = []
        for member in all_joined_day[str(w_i)]:
            if member not in data:
                data.append(member)
        temp_lurker = set(data)

    # remove newly active accounts from temp_lurker and store
    all_lurker[str(w_i)] = temp_lurker - all_new_active[str(w_i)]

    return all_lurker
