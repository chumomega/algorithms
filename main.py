from Graph import Graph
import GraphTraversals


def traverseObjectGraph():
    # TODO - Uncomment this code to try the common search algos on a Graph object(that stores edges)
    graph_instance = Graph({
        'a': ['b', 'c', 'd'],
        'd': ['b'],
        'c': ['a', 'd'],
        'b': ['a', 'c'],
    })
    GraphTraversals.bfs_on_object_graph(graph_instance, 'c')
    GraphTraversals.dfs_on_object_graph(graph_instance, 'c')


def traverseMatrixGraph():
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
if __name__ == '__main__':
    # 1 represents an edge btwn index i and j
    traverseObjectGraph()
    traverseMatrixGraph()
