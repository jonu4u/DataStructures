# 101. Symmetric Tree
# Given a binary tree, check whether it is a mirror of itself (ie, symmetric around its center).
#
# For example, this binary tree [1,2,2,3,4,4,3] is symmetric:
#
# 1
# / \
#     2   2
# / \ / \
#     3  4 4  3
#
#
# But the following [1,2,2,null,3,null,3] is not:
#
# 1
# / \
#     2   2
# \ \
#     3    3
#
#
# Follow up: Solve it both recursively and iteratively.

# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def isSymmetric(self, root):
        """
        :type root: TreeNode
        :rtype: bool
        """
        if not root:
            return True
        return self.check(root.left,root.right)


    def check(self,left_node,right_node):
        # If the left and right is None then its symmetric
        if not left_node and not right_node:
            return True
        # If both right and left is present check their value
        # if value equal then recurse on theor child as left of left and right of right_nodeand right of left and left of right
        elif left_node and right_node:
            if left_node.val== right_node.val:
                outer=self.check(left_node.left,right_node.right)
                inner=self.check(left_node.right,right_node.left)
                return outer and inner
            return False
        # All other cases are False
        else:
            return False