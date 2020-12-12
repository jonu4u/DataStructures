# 124. Binary Tree Maximum Path Sum
#
# Given a non-empty binary tree, find the maximum path sum.
#
# For this problem, a path is defined as any node sequence from some starting node to any node in the tree along the parent-child connections. The path must contain at least one node and does not need to go through the root.
#
#
#
# Example 1:
#    1
#   / \
#  2  3
#
# Input: root = [1,2,3]
# Output: 6
# Example 2:
#
#             -10
#             / \
#            9   20
#                / \
#               15  7
#
# Input: root = [-10,9,20,null,null,15,7]
# Output: 42
#
#
# Constraints:
#
# The number of nodes in the tree is in the range [0, 3 * 104].
# -1000 <= Node.val <= 1000

# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def __init__(self):
        self.ans=0
    def maxPathSum(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        # For one element return itself as sum
        if not root.left and not root.right:
            return root.val
        self.ans=float('-inf')
        self.dfs(root)
        return self.ans

    def dfs(self,root):
        if not root: return 0
        left=self.dfs(root.left)
        right=self.dfs(root.right)
        # If any value is less than 0 then it doesn't contribute to the sum so better to take it as 0 in the sum
        if left<0:
            left=0
        if right<0:
            right=0
        self.ans=max(self.ans,left+right+root.val)
        return max(left,right)+root.val

