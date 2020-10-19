# An undirected graph means each node has refernce to each node and viceversa
class Graph:
    def __init__(self):
        # initialize graph as a dict which is hashmap in python
        self.graph = {}

   # Since this is an undirected graph vertax A is linked to B and viceversa
    def addEdge(self,vertexA,vertexB):
        self.createEdge(vertexA,vertexB)
        self.createEdge(vertexB,vertexA)

    def createEdge(self,vertexA,vertexB):
        if vertexA in self.graph.keys():
            self.graph[vertexA].append(vertexB)
        else:
            self.graph[vertexA] = [vertexB]

    def removeVertex(self,vertex):
        return


# graph = Graph()
# graph.addEdge(0, 1)
# graph.addEdge(0, 2)
# graph.addEdge(0, 3)
# graph.addEdge(1, 2)
#
# print(graph.graph)