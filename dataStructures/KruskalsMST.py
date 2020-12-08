# Minimum spanning tree includes all vertices
class Graph:
    def __init__(self):
        self.parentMap={}
        self.currentIndex=0
        # This is needed for Kruskal not for union find
        self.graph =[]

    def add_edge(self,u,v,w):
        self.graph.append((u,v,w))
        is_u_present = False
        is_v_present = False
        for valueList in self.parentMap.values():
            if u in valueList:
                is_u_present=True
            if v in valueList:
                is_v_present=True
        if not is_u_present:
            self.add_vertex(u)
        if not is_v_present:
            self.add_vertex(v)

    def add_vertex(self,vertex):
        self.parentMap[self.currentIndex] = [vertex]
        self.currentIndex+=1


    def findParentKey(self,value):
        for key,eachValueList in self.parentMap.items():
            if value in eachValueList:
                return key

    def union(self,u,v):
        parentkey1 = self.findParentKey(u)
        parentkey2 = self.findParentKey(v)
        if parentkey1==parentkey2:
            return
        size1 = len(self.parentMap.get(parentkey1))
        size2 = len(self.parentMap.get(parentkey2))
        if(size1>size2):
            self.combine_groups(parentkey1,parentkey2)
        else:
            self.combine_groups(parentkey2,parentkey1)

    # Make key1 as key of 2nd group
    def combine_groups(self,key1,key2):
        value2= self.parentMap.get(key2)
        self.parentMap.get(key1).extend(value2)
        self.parentMap.pop(key2)

    def kruskal_algo(self):
        result=[]
        is_vertex_visited = set()
        self.graph= sorted(self.graph,key=lambda item:item[2])
        for u,v,w in self.graph:
            if u in is_vertex_visited and v in is_vertex_visited:
                continue
            is_vertex_visited.update([u,v])
            if len(self.parentMap)>1:
                self.union(u,v)
                result.append((u,v,w))
        return result

    def cost(self,result):
        cost=0
        for u,v,w in result:
            cost+=w
        return cost
# 14
g = Graph()
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
result = g.kruskal_algo()
print(result)
print(g.cost(result))