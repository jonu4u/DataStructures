# 314. Binary Tree Vertical Order Traversal
#
# Given a binary tree, return the vertical order traversal of its nodes' values. (ie, from top to bottom, column by column).
#
# If two nodes are in the same row and column, the order should be from left to right.
#
# Examples 1:
#
# Input: [3,9,20,null,null,15,7]
#
#       3
#      / \
#     9  20
#       / \
#      15   7
#
# Output:
#
# [
#     [9],
#     [3,15],
#     [20],
#     [7]
# ]
# Examples 2:
#
# Input: [3,9,8,4,0,1,7]
#
#         3
#        / \
#       9   8
#     /  \ / \
#     4  0 1   7
#
# Output:
#
# [
#     [4],
#     [9],
#     [3,0,1],
#     [8],
#     [7]
# ]
# Examples 3:
#
# Input: [3,9,8,4,0,1,7,null,null,null,2,5] (0's right child is 2 and 1's left child is 5)
#
#         3
#        / \
#       9   8
#      /  \/ \
#     4  0 1   7
#       / \
#      5   2
#
# Output:
#
# [
#     [4],
#     [9,5],
#     [3,0,1],
#     [8,2],
#     [7]
# ]
# Definition for a binary tree node.
from collections import deque
class TreeNode(object):
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution(object):
    def verticalOrder(self, root):
        """
        :type root: TreeNode
        :rtype: List[List[int]]
        """
        if not root:
            return root
        vertex_map=self.bfs(root)
        min_val=min(vertex_map.keys())
        max_val=max(vertex_map.keys())
        out_list=[]
        while min_val<=max_val:
            out_list.append(vertex_map.get(min_val))
            min_val+=1
        return out_list

    def bfs(self,root):
            q=deque()
            col_index=0
            q.append((root,col_index))
            vertex_map_with_col_index={}
            while len(q)>0:
                current_elem,current_col=q.popleft()
                if not vertex_map_with_col_index.get(current_col):
                    vertex_map_with_col_index[current_col]=[current_elem.val]
                else:
                    value_list=vertex_map_with_col_index.get(current_col).append(current_elem.val)
                    vertex_map_with_col_index[current_col]=value_list
                if current_elem.left:
                    q.append((current_elem.left,current_col-1))
                if current_elem.right:
                    q.append((current_elem.right,current_col+1))
            return vertex_map_with_col_index

#     543. Diameter of Binary Tree
#     Given a binary tree, you need to compute the length of the diameter of the tree.
#     The diameter of a binary tree is the length of the longest path between any two nodes in a tree. This path may or may not pass through the root.
#
# Example:
# Given a binary tree
#       1
#      / \
#     2   3
#    / \
#   4   5
# Return 3, which is the length of the path [4,2,1,3] or [5,2,1,3].
# Note: The length of path between two nodes is represented by the number of edges between them.

    def dia_tree(self,root):
        self.ans=1
        # depth of a node is a recursive function which is max of left height and right height
        def dfs(self,root):
            if not root:
                return 0
            left=self.dfs(root.left)
            right=self.dfs(root.right)
            # while we calculate depth each node and it's left and right constitutes a path.
            #     So length of the path is depth of left+depth of right +1(for the node itself)
            self.ans=max(self.ans,left+right+1)
            # Recursion call for finding depth
            return max(left,right) +1
        # Path is always total nodes -1
        return self.ans -1



