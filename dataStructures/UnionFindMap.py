class Graph:
    def __init__(self):
        self.parentMap={}
        self.currentIndex=0

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

# g = Graph()
# g.add_vertex(0)
# g.add_vertex(9)
# g.add_vertex(2)
# g.add_vertex(1)
# g.add_vertex(5)
# g.union(0,9)
# g.union(1,5)
# g.union(2,0)
# g.union(0,5)
# print(g.parentMap)

