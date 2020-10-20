class Graph:
    def __init__(self,items=[]):
        self.graph=[]
        self.size=[]
        for index,elem in enumerate(items):
            self.graph.append({index:elem})
            self.size.append({index:1})

    def union(self,value1,value2):
        parent1key = list(self.find(value1))[0]
        parent2key = list(self.find(value2))[0]
        # Already in same group do nothing
        if parent1key==parent2key:
            return
        size1=self.size[parent1key].get(parent1key)
        size2=self.size[parent2key].get(parent2key)
        if(size1>size2):
            self.unionGroups(parent1key,parent2key)
        else:
            self.unionGroups(parent2key,parent1key)

   # make parent1key as key of parent2group and increase size of group of parent1
    def unionGroups(self,parentkey1,parentkey2):
        for index,elem in enumerate(self.graph):
            if list(elem.keys())[0] == parentkey2:
                self.graph[index] = {parentkey1:elem.get(parentkey2)}
                self.size[parentkey1]={parentkey1:(self.size[parentkey1].get(parentkey1)+1)}
                self.size[parentkey2]={parentkey2:(self.size[parentkey2].get(parentkey2)-1)}
                if self.size[parentkey2].get(parentkey2)==0:
                    self.size[parentkey2]=None


    def findSize(self):
        def cond(letter):
            if letter is not None:
                return True
            else:
                return False
        filtered = filter(cond,self.size)
        return len(list(filtered))




    def find(self,value):
        rootKey = None
        for elem in self.graph:
            rootKey=list(elem.keys())[0]
            if elem.get(rootKey)==value:
                break
        for elem in self.graph:
            if rootKey == list(elem.keys())[0]:
                return elem


# graph=Graph([1,12,4,7,8])
# graph.union(12,4)
# print(graph.graph)
# print(graph.size)
# graph.union(7,8)
# graph.union(12,1)
# print(graph.graph)
# print(graph.size)
# graph.union(7,4)
# print(graph.graph)
# print(graph.size)
# print(graph.findSize())

# # Test Find
# graph.graph=[{0:1},{1:2},{2:34},{0:6},{0:7},{1:8},{2:12},{1:9}]
# print(graph.find(12))
