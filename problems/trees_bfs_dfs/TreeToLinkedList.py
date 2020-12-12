# 114. Flatten Binary Tree to Linked List
#
# Given a binary tree, flatten it to a linked list in-place.
#
# For example, given the following tree:
#
#        1
#       / \
#      2   5
#     / \   \
#     3   4   6
# The flattened tree should look like:
#
# 1
#  \
#   2
#    \
#     3
#      \
#       4
#        \
#         5
#          \
#           6

class TreeNode(object):
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution(object):
    def flatten(self, root):
        """
        :type root: TreeNode
        :rtype: None Do not return anything, modify root in-place instead.
        """
        if root is None:
            return root
        preorder=self.preorder(root,[])
        # For each element the right node is the next node and the left node is null
        index=0
        while index < len(preorder)-1:
            preorder[index].left=None
            preorder[index].right=preorder[index+1]
            index+=1

    # Return a list where tree nodes in order
    def preorder(self,root,list1):
        if root is None:
            return
        list1.append(root)
        self.preorder(root.left,list1)
        # prev.left=None
        self.preorder(root.right,list1)
        return list1