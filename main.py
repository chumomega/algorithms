from Graph import Graph
from TreeTraversals import createMockTree
from TreeTraversals import bfs_on_tree
from TreeTraversals import printTreeInOrder
import GraphTraversals


def traverseObjectGraph():
    # TODO - Uncomment this code to try the common search algos on a Graph object(that stores edges)
    graph_instance = Graph(
        {
            "a": ["b", "c", "d"],
            "d": ["b"],
            "c": ["a", "d"],
            "b": ["a", "c"],
        }
    )
    GraphTraversals.bfs_on_object_graph(graph_instance, "c")
    GraphTraversals.dfs_on_object_graph(graph_instance, "c")


def traverseMatrixGraph():
    # 1 represents an edge btwn index i and j
    matrix_graph = [
        [0, 1, 1, 0, 0],
        [1, 0, 1, 1, 0],
        [1, 1, 0, 1, 0],
        [0, 1, 1, 0, 0],
        [0, 0, 0, 0, 0],
    ]

    GraphTraversals.bfs_on_am_graph(matrix_graph, 3)
    GraphTraversals.dfs_on_am_graph(matrix_graph, 3)


# Press the green button in the gutter to run the script.
if __name__ == "__main__":

    # Graph Traversal algorithms!
    # traverseObjectGraph()
    # traverseMatrixGraph()

    # Tree Traversal algorithms!
    mock_tree = createMockTree()
    printTreeInOrder(mock_tree)
    bfs_on_tree(mock_tree)
