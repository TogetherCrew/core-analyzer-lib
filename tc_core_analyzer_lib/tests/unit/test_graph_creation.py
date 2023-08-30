import numpy as np
from tc_core_analyzer_lib.utils.generate_graph import make_graph


def test_graph_creation():
    """
    test if a graph created right
    """
    interaction_mtx = np.array([[0, 1, 1], [1, 0, 3], [2, 2, 0]])

    graph = make_graph(interaction_mtx)

    assert list(graph.nodes) == [0, 1, 2]
    assert np.all(
        np.array(graph.edges) == [[0, 1], [0, 2], [1, 0], [1, 2], [2, 0], [2, 1]]
    )
