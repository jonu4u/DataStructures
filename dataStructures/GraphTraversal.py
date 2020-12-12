from collections import deque
class Node:
    def __init__(self,value):
        self.value=value
        self.neighbors=[]

class Graph:
    def __init__(self):
        self.vertices={}
        self.head=None
        self.matrix=[]

    def add_vertex(self,vertex_value):
        vertex=Node(vertex_value)
        if vertex in self.vertices:
            return False
        else:
            self.vertices[vertex_value]=vertex
            return True

    def get_node_value(self,node):
        return node.value

    def add_edge(self,u,v):
        if u in self.vertices and v  in self.vertices:
            # add v as neighbour of u
            self.vertices.get(u).neighbors.append(self.vertices.get(v))
            sorted(self.vertices.get(u).neighbors,key=self.get_node_value)
            # add u as neighbour of v
            self.vertices.get(v).neighbors.append(self.vertices.get(u))
            sorted(self.vertices.get(v).neighbors,key=self.get_node_value)


    def bfs(self,root):
        q=deque()
        is_vertex_traversed=set()
        q.append(root)
        out_list=[]
        while len(q)>0:
            current=q.popleft()
            if current.value not in is_vertex_traversed:
                is_vertex_traversed.add(current.value)
                out_list.append(current.value)
                neighbors=self.vertices.get(current.value).neighbors
                q.extend(neighbors)
        return out_list

    def dfs(self,root):
        stack=[]
        stack.append(root)
        out_list=[]
        is_visited=set()
        while len(stack)>0:
            current=stack.pop(0)
            if current.value not in is_visited:
                is_visited.add(current.value)
                out_list.append(current.value)
                self.vertices.get(current.value).neighbors.reverse()
                for neighbour in self.vertices.get(current.value).neighbors :
                    stack=[neighbour]+stack
        return out_list

    # Try traversals for adjacency matrix
    def dfs_matrix(self):
        return


    def bfs_matrix(self):
        return







g=Graph()
a=Node('A')
g.head=a
g.add_vertex(a)
# ord takes the unicode of a char.Now i becomes unicode, so chr(i)
# again converts it to character.
for i in range(ord('A'),ord('K')):
    g.add_vertex(chr(i))

edges=['AB','AE','BF','CG','DE','DH','EH','FG','FI','FJ','GJ','HI']
for i in edges:
    g.add_edge(i[:1],i[1:])

print(g.bfs(g.head))
print(g.dfs(g.head))





