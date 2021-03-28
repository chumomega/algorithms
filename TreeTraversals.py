import queue
from Graph import Graph

# input - list of lists - adjacency matrix
def bfs_on_am_graph(graph: list, start: int):
    print("Beginning Breadth first search on matrix graph...")
    if len(graph) is 0:
        return
    visited = set()
    to_visit_queue = queue.Queue()
    to_visit_queue.put(start)

    while not to_visit_queue.empty():
        # we take the next node off the queue to explore it's neighbors (1 node away)
        node = to_visit_queue.get()

        if node not in visited:
            print("Explore node on matrix graph w/ BFS : ", node)

            for neighbor in range(len(graph[node])):
                # if we have an edge and haven't visited yet
                if graph[node][neighbor] == 1 and neighbor not in visited:
                    to_visit_queue.put(neighbor)
            visited.add(node)
    return


# input - list of lists - adjacency matrix
def dfs_on_am_graph(graph: list, start: int, visited=None):
    # failsafe checks, this shouldn't happen tho
    if len(graph) == 0 or start > len(graph) - 1:
        return

    if visited is None:
        print("Beginning Depth first search on matrix graph...")
        visited = set()

    visited.add(start)
    print("Explore node on matrix graph w/ DFS : ", start)

    for neighbor in range(len(graph[start])):
        if neighbor not in visited and graph[start][neighbor] == 1:
            dfs_on_am_graph(graph, neighbor, visited)


# input - graph object
def bfs_on_object_graph(graph: Graph, start: str):
    # if len(graph) is 0:
    #     return
    print("Beginning Breadth first search on object graph...")
    visited = set()
    to_visit_queue = queue.Queue()
    to_visit_queue.put(start)

    while not to_visit_queue.empty():
        # we take the next node off the queue to explore it's neighbors (1 node away)
        node = to_visit_queue.get()

        if node not in visited:
            print("Explore node on object graph w/ BFS : ", node)

            for neighbor in graph.getConnectedNodes(node):
                # if we have an edge and haven't visited yet
                if neighbor not in visited:
                    to_visit_queue.put(neighbor)
            visited.add(node)
    return


# input - graph object
def dfs_on_object_graph(graph: Graph, start: str, visited=None):
    nodes = graph.getVertices()
    if len(nodes) == 0 or start not in nodes:
        return

    if visited is None:
        # should be first time being called
        print("Beginning Depth first search on object graph...")
        visited = set()

    if start not in visited:
        print("Explore node on object graph w/ DFS : ", start)

        visited.add(start)
        neighbors = graph.getConnectedNodes(start)

        for neighbor in neighbors:
            # we want to search the depth of every node we have not visited yet
            if neighbor not in visited:
                dfs_on_object_graph(graph, neighbor, visited)
