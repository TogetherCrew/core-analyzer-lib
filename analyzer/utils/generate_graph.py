import numpy as np
from networkx import DiGraph, from_numpy_array


def make_graph(matrix: np.ndarray) -> DiGraph:
    """
    Turns interaction matrix into a directed graph object

    Parameters:
    --------------
    matrix : np.ndarray
        the interaction matrix

    Returns:
    -----------
    graph : networkx.DiGraph object
        the graph generated directly from the matrix
    """
    graph = from_numpy_array(matrix, create_using=DiGraph)

    return graph
