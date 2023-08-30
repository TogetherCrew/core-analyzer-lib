def check_prev_period(engagement_dict: dict[str, set[str]], time_str: str) -> set[str]:
    """
    Checks if values are present in specific previous period of dict

    Parameters:
    ------------
    engagement_dict : dict[str, set[str]]
        dictionary with account names sets
        as values for periods indicated as keys
    time_str : str
        dictionary key of interest

    Returns:
    ----------
    temp_set : set[str]
        either the set that is the value for the time_str
        key or and empty set
    """

    # if engagement_dict contains data for time_str
    if time_str in engagement_dict.keys():
        temp_set = set(engagement_dict[time_str])
    else:
        temp_set = set("")

    return temp_set
