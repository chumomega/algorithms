from Graph import Graph
from TreeNode import TreeNode
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


def createMockTree() -> TreeNode:
    node_1 = TreeNode('a')
    node_2 = TreeNode('b')
    node_3 = TreeNode('c')
    node_4 = TreeNode('d')
    node_5 = TreeNode('e')
    node_6 = TreeNode('f')
    node_7 = TreeNode('g')
    node_8 = TreeNode('h')
    node_9 = TreeNode('i')

    node_1.left = node_2
    node_1.right = node_3

    node_2.left = node_4
    node_2.right = node_5

    node_3.left = node_6
    node_3.right = node_7

    node_5.left = node_8
    node_7.right = node_9

   #            a
   #     b             c
   # d       e     f       g
   #       h                  i

    return node_1


def printTreeInOrder(root: TreeNode):
    # there is in order, pre order, post order
    # you just need to change the order of this code!
    # no cycles in trees
    if root.left is not None:
        printTreeInOrder(root.left)
    print("In order: ", root.value)

    if root.right is not None:
        printTreeInOrder(root.right)


def bfs_on_tree(root: TreeNode):
    node_queue = [root]

    while len(node_queue) != 0:
        node = node_queue.pop(0)
        print("Node: ", node.value)

        if node.left is not None:
            node_queue.append(node.left)
        if node.right is not None:
            node_queue.append(node.right)
    return


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    # 1 represents an edge btwn index i and j
    # traverseObjectGraph()
    # traverseMatrixGraph()

    mock_tree = createMockTree()
    # printTreeInOrder(mock_tree)
    bfs_on_tree(mock_tree)
