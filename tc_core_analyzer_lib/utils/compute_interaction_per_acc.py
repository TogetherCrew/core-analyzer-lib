import copy

import numpy as np
import numpy.typing as npt
from networkx import DiGraph

from .generate_graph import make_graph


def thr_int(
    int_mat: dict[str, np.ndarray],
    INT_THR: int,
    UW_DEG_THR: int,
    EDGE_STR_THR: int,
    UW_THR_DEG_THR: int,
    activities: list[str],
    **kwargs,
) -> tuple[
    npt.NDArray[np.int32], npt.NDArray[np.int32], npt.NDArray[np.int32], DiGraph
]:
    """
    Computes number of interactions and connections per account

    Parameters:
    ------------
    int_mat : dict[str, np.ndarray[int]]
        dictionary of keys as activities and values as
        2D weighted directed interaction matrix
        must be squared matrix to have all the interaction between all users
    INT_THR : int
        minimum number of interactions to be active
    UW_DEG_THR : int
        minimum number of connections to be active
    EDGE_STR_THR : int
        minimum number of interactions for connected
    UW_THR_DEG_THR : int
        minimum number of accounts for connected
    activities : list[str]
        the activities to get from int_matrix.
        Note: the `int_mat` should have the keys of given activities
    kwargs :
        ignore_axis_0_activities : list[str]
            ignore the axis zero of matrix of given activites
        ignore_axis_1_activities : list[str]
            ignore the axis one of matrix of given activites

    Returns:
    ---------
    thr_ind : npt.NDArray[np.int32]
        index numbers of account names with at least
        INT_THR interactions
    thr_uw_deg : npt.NDArray[np.int32]
        index numbers of account names with at least
        UW_DEG_THR connections
    thr_uw_thr_deg : npt.NDArray[np.int32]
        index numbers of account names with at
        least UW_THR_DEG_THR connections of at least EDGE_STR_THR
        interactions each
    graph : networkx.DiGraph
        the network graph of active members
    """

    ignore_axis_0_activities: list[str]
    ignore_axis_1_activities: list[str]

    if "ignore_axis_0_activities" not in kwargs:
        ignore_axis_0_activities = []
    else:
        ignore_axis_0_activities = kwargs["ignore_axis_0_activities"]
    if "ignore_axis_1_activities" not in kwargs:
        ignore_axis_1_activities = []
    else:
        ignore_axis_1_activities = kwargs["ignore_axis_1_activities"]

    int_analysis = get_analysis_vector(
        int_mat=int_mat,
        activites=activities,
        ignore_axis_0_activities=ignore_axis_0_activities,
        ignore_axis_1_activities=ignore_axis_1_activities,
    )

    # turn int_mat from all interaction types into graph
    # all the activities has the same interaction matrix
    # with the same shape
    matrix = np.zeros_like(int_mat[activities[0]])

    for activity in activities:
        matrix += int_mat[activity]

    graph = make_graph(matrix)

    # # # TOTAL INTERACTIONS # # #

    # compare total active interactions to active interaction threshold
    thr_ind = np.where(int_analysis >= INT_THR)[0]

    # # # TOTAL CONNECTIONS # # #

    # get unweighted node degree value for each node
    all_degrees = np.array([val for (node, val) in graph.degree()])

    # compare total unweighted node degree to interaction threshold
    thr_uw_deg = np.where(all_degrees >= UW_DEG_THR)[0]

    # # # THRESHOLDED CONNECTIONS # # #

    # make copy of graph for thresholding
    thresh_graph = copy.deepcopy(graph)

    # remove edges below threshold from copy
    thresh_graph.remove_edges_from(
        [
            (n1, n2)
            for n1, n2, w in thresh_graph.edges(data="weight")
            if w < EDGE_STR_THR
        ]
    )

    # get unweighted node degree value for each node from thresholded network
    all_degrees_thresh = np.array([val for (node, val) in thresh_graph.degree()])

    # compare total unweighted node degree after thresholding to threshold
    thr_uw_thr_deg = np.where(all_degrees_thresh > UW_THR_DEG_THR)[0]

    return (thr_ind, thr_uw_deg, thr_uw_thr_deg, graph)


def get_analysis_vector(
    int_mat: dict[str, np.ndarray],
    activites: list[str],
    ignore_axis_0_activities: list[str],
    ignore_axis_1_activities: list[str],
):
    """
    compute the analysis vector based on given matrixes

    Parameters:
    -------------
    int_mat : dict[str, np.ndarray[int]]
        dictionary of keys as activities and values as
        2D weighted directed interaction matrix
    activities : list[str]
        the activities to get from int_matrix.
        Note: the `int_mat` should have the keys of given activities
    ignore_axis_0_activities : list[str]
        ignore the axis zero of matrix of given activites
        can be an empty list
    ignore_axis_1_activities : list[str]
        ignore the axis one of matrix of given activites
        can be an empty list
    """
    user_count = int_mat[activites[0]].shape[0]

    # creating the zero analysis vector for all users
    int_analysis = np.zeros(user_count)

    for activity in activites:
        # A flag to see check the activity is not in both ignore lists
        flag: bool = True

        if activity in ignore_axis_0_activities:
            int_analysis += np.sum(int_mat[activity], axis=1)
            flag = False

        if activity in ignore_axis_1_activities:
            int_analysis += np.sum(int_mat[activity], axis=0)
            flag = False

        # if the activity was not ignored in both axis
        # we should include both axis
        if flag:
            int_analysis += np.sum(int_mat[activity], axis=0) + np.sum(
                int_mat[activity], axis=1
            )

    return int_analysis
