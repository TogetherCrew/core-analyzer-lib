from collections import Counter


def check_past(
    data_dic: dict[str, set[str]], t_thr: int, o_thr: int, WINDOW_D: int
) -> set[str]:
    """
    Checks in how many previous periods account names were in a dict

    Parameters:
    -------------
    data_dic : dict[str, set[str]]
        dictionary with account name sets to check
    t_thr : int
        number of time period into the past to consider
    o_thr : int
        minimal number of occurences of account name within
        the period specified by t_thr
    WINDOW_D : int
        width of an analysis window in number of days

    Returns:
    ---------
    acc_selection : set[str]
        all accounts that were present in data_dic
        for more than `o_thr` times within the last `t_thr` periods
    """

    # initiate empty result list
    acc_per_period = []

    # obtain dictionary keys
    dic_keys = list(data_dic.keys())

    # for each period that should be considered
    for p in range(t_thr):
        # if time period is present in dic_keys
        if len(dic_keys) >= -(-1 - (p * WINDOW_D)):
            # obtain accounts in period
            acc_per_period.append(list(data_dic[str(dic_keys[-1 - (p * WINDOW_D)])]))

        else:
            # store empty values
            acc_per_period.append([])

    # merge values in list of list into single list
    all_acc_list = [elem for sublist in acc_per_period for elem in sublist]

    # count number of occurences in list per account
    acc_cnt_dict = Counter(all_acc_list)

    # obtain account names that with at least o_thr occurences in all_acc_list
    acc_selection: set[str] = set(
        [acc for acc, occurrences in acc_cnt_dict.items() if occurrences >= o_thr]
    )

    return acc_selection
