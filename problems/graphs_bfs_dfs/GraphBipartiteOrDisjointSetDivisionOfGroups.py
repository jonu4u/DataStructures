# 785. Is Graph Bipartite?
#
# Given an undirected graph, return true if and only if it is bipartite.
#
# Recall that a graph is bipartite if we can split its set of nodes into two independent subsets A and B, such that every edge in the graph has one node in A and another node in B.
#
# The graph is given in the following form: graph[i] is a list of indexes j for which the edge between nodes i and j exists.  Each node is an integer between 0 and graph.length - 1.  There are no self edges or parallel edges: graph[i] does not contain i, and it doesn't contain any element twice.
#
#
#
# Example 1:
#
#
# Input: graph = [[1,3],[0,2],[1,3],[0,2]]
# Output: true
# Explanation: We can divide the vertices into two groups: {0, 2} and {1, 3}.
#
# Example 2:
#
#
# Input: graph = [[1,2,3],[0,2],[0,1,3],[0,2]]
# Output: false
# Explanation: We cannot find a way to divide the set of nodes into two independent subsets.
#
#
#
# Constraints:
#
# 1 <= graph.length <= 100
# 0 <= graph[i].length < 100
# 0 <= graph[i][j] <= graph.length - 1
# graph[i][j] != i
# All the values of graph[i] are unique.
# The graph is guaranteed to be undirected.
#
# https://www.youtube.com/watch?v=0ACfAqs8mm0

from collections import deque
from collections import defaultdict
class Solution(object):
    def isBipartite(self, graph):
        """
        :type graph: List[List[int]]
        :rtype: bool
        """

        # Let us define two colors 0 and 1
        color_map={}
        color=0
        sz=len(graph)
        is_visited=set()
        # We'll do DFS for each node and put them in is_visited when done'
        for vertex in range(sz):
            if vertex not in is_visited:
                # This stack will be used for DFS
                stack=deque()
                stack.append(vertex)
                # We put mark this node as visited
                is_visited.add(vertex)
                # We also put the vertex and assign color to it
                color_map[vertex]=color
                # We start DFS for this node here
                while stack:
                    curr=stack.popleft()
                    adj_list=graph[curr]
                    # Any node which is in q must be in color map
                    parent_color=color_map[curr]
                    for neighbour in adj_list:
                        # If we have not visited the neighbour, let's put in q
                        # for doing DFS of that node and it's children
                        # and park the parent as is_visited. Also put the color of the child as opposite of
                        # parent
                        if neighbour not in is_visited:
                            is_visited.add(neighbour)
                            stack.appendleft(neighbour)
                            color_map[neighbour]=self.rev(parent_color)
                        # Here we check that any neighbour if present in
                        # map and already visited must have color rev to parent,
                        # if not we return false
                        if color_map[neighbour]!=self.rev(parent_color):
                            return False
        return True


    def rev(self,color):
        if color==1:
            return 0
        return 1

s=Solution()
print(s.isBipartite([[1,3],[0,2],[1,3],[0,2]]))
print(s.isBipartite(graph = [[1,2,3],[0,2],[0,1,3],[0,2]]))
print(s.isBipartite(graph = [[1],[0,3],[3],[1,2]]))
