from dataStructures import UnionFind_DisjointSet
class Krushkal:
    def __init__(self):
        self.graph=[]
        self.sorted_list=[]

    def add_edge(self,u,v,w):
        self.graph.append((u,v,w))

    def sort_graph_on_weight(self):
        self.graph=sorted(self.graph,key=lambda item:item[2])
        for u,v,w in self.graph:
            if u not in self.sorted_list:
                self.sorted_list.append(u)
            if v not in self.sorted_list:
                self.sorted_list.append(v)

    def krushkal_algo(self):
        result=[]
        is_node_visited=set()
        self.sort_graph_on_weight()
        graph = UnionFind_DisjointSet.Graph(self.sorted_list)
        for u,v,w in self.graph:
            if u in is_node_visited and v in is_node_visited:
                continue
            is_node_visited.add(u)
            is_node_visited.add(v)
            graph.union(u,v)
            result.append((u,v,w))
            if(graph.findSize()==1):
                break;

        return result

    def cost(self,result):
        cost = 0
        for elem in result:
            cost=cost+elem[2]
        return cost


# Test programwiz example
g = Krushkal()
g.add_edge(0, 1, 4)
g.add_edge(0, 2, 4)
g.add_edge(1, 2, 2)
g.add_edge(1, 0, 4)
g.add_edge(2, 0, 4)
g.add_edge(2, 1, 2)
g.add_edge(2, 3, 3)
g.add_edge(2, 5, 2)
g.add_edge(2, 4, 4)
g.add_edge(3, 2, 3)
g.add_edge(3, 4, 3)
g.add_edge(4, 2, 4)
g.add_edge(4, 3, 3)
g.add_edge(5, 2, 2)
g.add_edge(5, 4, 3)
result = g.krushkal_algo()
print(result)
print(g.cost(result))