class Graph:

    graph_dict = None

    def __init__(self, graph_dict=None):
        if graph_dict is None:
            self.graph_dict = {}
        else:
            self.graph_dict = graph_dict

    def getConnectedNodes(self, vertex: str):
        if vertex in self.graph_dict:
            return self.graph_dict[vertex]
        return None

    def getVertices(self):
        return self.graph_dict.keys()

    def addVertex(self, vertex: str):
        if vertex in self.graph_dict:
            return False
        else:
            self.graph_dict[vertex] = []
            return True
