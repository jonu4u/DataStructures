# 133. Clone Graph
# Given a reference of a node in a connected undirected graph.
#
# Return a deep copy (clone) of the graph.
#
# Each node in the graph contains a val (int) and a list (List[Node]) of its neighbors.
#
# class Node {
# public int val;
# public List<Node> neighbors;
# }
#
#
# Test case format:
#
# For simplicity sake, each node's value is the same as the node's index (1-indexed). For example, the first node with val = 1, the second node with val = 2, and so on. The graph is represented in the test case using an adjacency list.
#
# Adjacency list is a collection of unordered lists used to represent a finite graph. Each list describes the set of neighbors of a node in the graph.
#
# The given node will always be the first node with val = 1. You must return the copy of the given node as a reference to the cloned graph.
#
#
#
# Example 1:
#
#
# Input: adjList = [[2,4],[1,3],[2,4],[1,3]]
# Output: [[2,4],[1,3],[2,4],[1,3]]
# Explanation: There are 4 nodes in the graph.
# 1st node (val = 1)'s neighbors are 2nd node (val = 2) and 4th node (val = 4).
# 2nd node (val = 2)'s neighbors are 1st node (val = 1) and 3rd node (val = 3).
# 3rd node (val = 3)'s neighbors are 2nd node (val = 2) and 4th node (val = 4).
# 4th node (val = 4)'s neighbors are 1st node (val = 1) and 3rd node (val = 3).
# Example 2:
#
#
# Input: adjList = [[]]
# Output: [[]]
# Explanation: Note that the input contains one empty list. The graph consists of only one node with val = 1 and it does not have any neighbors.
# Example 3:
#
# Input: adjList = []
# Output: []
# Explanation: This an empty graph, it does not have any nodes.
# Example 4:
#
#
# Input: adjList = [[2],[1]]
# Output: [[2],[1]]
# Definition for a Node.
class Node(object):
    def __init__(self, val = 0, neighbors = None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []

class Solution(object):
    def cloneGraph_naive(self, node):
        if node is None:
            return node
        # take map which keeps adjacency list of old graph for each vertex
        vertex_map={}
        # populate the map with recursion
        self.add_vertex(node,vertex_map)
        # Take another map and start populating it with key as each vertex and value as a new node
        visited={}
        size=len(vertex_map)
        while size>0:
            # if the node is not present add as a new node to the new map
            if visited.get(size) is None:
                visited[size]=Node(size)
            neighbors=[]
            # Add the neighbors.Also check neighbors from new map if not present create the neighbors
            for elem in vertex_map.get(size).neighbors:
                if visited.get(elem.val) is None:
                    visited[elem.val]=Node(elem.val)
                neighbors.append(visited.get(elem.val))
            visited[size].neighbors=neighbors
            # Do this for all vertices pf the graph
            size-=1
        # return the 1st node as per problem
        return visited.get(1)


    def add_vertex(self,node,map):
        is_node_present=False
        # If vertex is not added add in map as vetex val as key and node as value
        if map.get(node.val) is None:
            is_node_present=True
            map[node.val]=node
        if is_node_present:
            return
        for neighbour in node.neighbors:
            self.add_vertex(neighbour,map)


s=Solution()
node1=Node(1)
node2=Node(2)
node3=Node(3)
node4=Node(4)
node1.neighbors=[node2,node4]
node2.neighbors=[node1,node3]
node3.neighbors=[node2,node4]
node4.neighbors=[node1,node3]
s.cloneGraph_naive(node1)