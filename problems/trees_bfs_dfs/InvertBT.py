# 226. Invert Binary Tree
# Invert a binary tree.
#
# Example:
#
# Input:
#
#         4
#        / \
#       2    7
#      / \   / \
#     1   3 6   9
# Output:
#
#         4
#        /  \
#       7     2
#      / \   / \
#     9   6 3   1
# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution(object):
    def invertTree(self, root):
        """
        :type root: TreeNode
        :rtype: TreeNode
        """
        return self.post_order(root)

    def post_order(self, root):
        if not root:return
        self.post_order(root.left)
        self.post_order(root.right)
        return self.swap_child_of_node(root)

    def swap_child_of_node(self,node):
        if node.left and node.right:
            node.left,node.right=node.right,node.left
        elif not node.right and node.left:
            node.right=node.left
            node.left=None
        elif node.right and not node.left:
            node.left=node.right
            node.right=None
        return node

s=Solution()
n1=TreeNode(4)
n2=TreeNode(2)
n3=TreeNode(7)
n4=TreeNode(1)
n5=TreeNode(3)
n6=TreeNode(6)
n7=TreeNode(9)
n1.left=n2
n1.right=n3
n2.left=n4
n2.right=n5
n3.left=n6
n3.right=n7
s.invertTree(n1)
