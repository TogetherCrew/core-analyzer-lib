from networkx import from_numpy_array, DiGraph
import numpy as np


def make_graph(matrix: np.ndarray):
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
