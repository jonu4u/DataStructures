# 863. All Nodes Distance K in Binary Tree
#
# We are given a binary tree (with root node root), a target node, and an integer value K.
#
# Return a list of the values of all nodes that have a distance K from the target node.  The answer can be returned in any order.
#
#
#
# Example 1:
#
# Input: root = [3,5,1,6,2,0,8,null,null,7,4], target = 5, K = 2
#
# Output: [7,4,1]
#
# Explanation:
# The nodes that are a distance 2 from the target node (with value 5)
# have values 7, 4, and 1.
#
#
#
# Note that the inputs "root" and "target" are actually TreeNodes.
# The descriptions of the inputs above are just serializations of these objects.
#
#
# Note:
#
# The given tree is non-empty.
# Each node in the tree has unique values 0 <= node.val <= 500.
# The target node is a node in the tree.
# 0 <= K <= 1000.
# Definition for a binary tree node.
from collections import defaultdict,deque
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

# For this problem we have to convert the TREE TO GRAPH. THEN FOR THE graph do BFS on Level K to get the answer
class Solution(object):
    def distanceK(self, root, target, K):
        """
        :type root: TreeNode
        :type target: TreeNode
        :type K: int
        :rtype: List[int]
        """
        # This is the graph in adjacency list format where each node is the vertex and the left,rght and root are its neighbours
        tree_graph=self.preorder(root,defaultdict(set),None)
        is_visited=set()
        # We do BFS on level K for this graph
        q=deque()
        level=0
        # We start with target and after every BFS we mark end of level as None
        q.append(target.val)
        q.append(None)
        out=[]
        while q:
            curr=q.popleft()
            # If we have exhausted the graph or we reached level more than K we break
            if level>K or len(is_visited)==len(tree_graph):
                break
            # When we get None we increase level by 1 and mark end of level of its neighbours
            if curr is None:
                level+=1
                q.append(None)
                continue
            # When desired level is reached we append to output list
            if level==K:
                out.append(curr)

            is_visited.add(curr)
            adj_list=tree_graph[curr]
            for nei in adj_list:
                if nei not in is_visited:
                    q.append(nei)
        return out

    # Doing DFS traversal we convert the tree to a undirected graph, with each vertex as node and parent,left,right as neighbours
    def preorder(self,root,graph,parent):
        if not root: return graph
        if parent:
           graph[root.val].add(parent.val)
        if root.left:
            graph[root.val].add(root.left.val)
        if root.right:
            graph[root.val].add(root.right.val)
        graph=self.preorder(root.left,graph,root)
        graph=self.preorder(root.right,graph,root)
        return graph
