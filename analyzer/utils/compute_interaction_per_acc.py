import copy
from typing import Any

import numpy as np

from .activity import Activity
from .generate_graph import make_graph


def thr_int(
    int_mat: dict[Activity, np.ndarray],
    INT_THR: int,
    UW_DEG_THR: int,
    EDGE_STR_THR: int,
    UW_THR_DEG_THR: int,
) -> tuple[
    np.ndarray[Any, np.dtype[np.signedinteger[Any]]],
    np.ndarray[Any, np.dtype[np.signedinteger[Any]]],
    np.ndarray[Any, np.dtype[np.signedinteger[Any]]],
    Any,
]:
    """
    Computes number of interactions and connections per account

    Parameters:
    ------------
    int_mat : dict[Activity, np.ndarray[int]]
        dictionary of keys as activities and values as
        2D weighted directed interaction matrix
    INT_THR : int
        minimum number of interactions to be active
    UW_DEG_THR : int
        minimum number of connections to be active
    EDGE_STR_THR : int
        minimum number of interactions for connected
    UW_THR_DEG_THR : int
        minimum number of accounts for connected

    Returns:
    ---------
    thr_ind : list[int]
        index numbers of account names with at least
        INT_THR interactions
    thr_uw_deg : list[int]
        index numbers of account names with at least
        UW_DEG_THR connections
    thr_uw_thr_deg : list[int]
        index numbers of account names with at
        least UW_THR_DEG_THR connections of at least EDGE_STR_THR
        interactions each
    """

    # # # SELECT DATA FROM INT_MAT # # #

    # select number of active interactions per account
    int_analysis = (
        np.sum(int_mat[Activity.Reply], axis=0)
        + np.sum(int_mat[Activity.Reply], axis=1)
        + np.sum(int_mat[Activity.Reaction], axis=0)
        + np.sum(int_mat[Activity.Reaction], axis=1)
        + np.sum(int_mat[Activity.Mention], axis=1)
    )

    # turn int_mat from all interaction types into graph
    graph = make_graph(
        int_mat[Activity.Reply] + int_mat[Activity.Reaction] + int_mat[Activity.Mention]
    )

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
