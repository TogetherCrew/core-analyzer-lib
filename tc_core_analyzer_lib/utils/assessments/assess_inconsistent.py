def assess_inconsistent(
    all_active: dict[str, set[str]],
    all_paused: dict[str, set[str]],
    all_new_active: dict[str, set[str]],
    all_consistent: dict[str, set[str]],
    w_i: int,
) -> dict[str, set[str]]:
    """
    assess inconsistently active members base on the given input sets

    Parameters
    ------------
    all_active : dict[str, set[str]]
        dictionary with keys w_i and values
        containing a set of all account names that are active
    all_paused : dict[str, set[str]]
        dictionary with keys w_i and values
        containing a set of all account names that are paused
    all_new_active : dict[str, set[str]]
        dictionary with keys w_i and values
        containing a set of all account names that are active for first time
    all_consistent : dict[str, set[str]]
        dictionary with keys w_i and values
        containing a set of all account names that are consistently active
    w_i : int
        index of sliding time window

    Returns
    ---------
    all_inconsistent : set[str]
        containing a set of all account names that are inconsistently active
    """
    all_inconsistent = (
        all_active[str(w_i)].union(all_paused[str(w_i)])
        - all_new_active[str(w_i)]
        - all_consistent[str(w_i)]
    )

    return all_inconsistent
