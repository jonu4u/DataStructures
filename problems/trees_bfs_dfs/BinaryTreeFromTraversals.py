# 105. Construct Binary Tree from Preorder and Inorder Traversal
#
# Given preorder and inorder traversal of a tree, construct the binary tree.
#
# Note:
# You may assume that duplicates do not exist in the tree.
#
# For example, given
#
# preorder = [3,9,20,15,7]
# inorder = [9,3,15,20,7]
# Return the following binary tree:
#
#       3
#      / \
#     9  20
#        / \
#       15   7
# https://www.youtube.com/watch?v=PoBGyrIWisE
class TreeNode(object):
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution(object):
    def buildTree(self, preorder, inorder):
        """
        :type preorder: List[int]
        :type inorder: List[int]
        :rtype: TreeNode
        """
        preorder_index=0
        inorder_map={val:index for index,val in enumerate(inorder)}
        def helper(left=0,right=len(inorder)):
            nonlocal preorder_index
            if left==right:
                return None
            root=TreeNode(preorder[preorder_index])
            preorder_index+=1
            # get the root index from the inorder_root map
            # and we again put in helper the left subtree index and the
            # right subtree index.
            split_index=inorder_map[root.val]
            root.left=helper(left,split_index)
            root.right=helper(split_index+1,right)
            # We construct left and right tree till the inorder list is none and we pick the order from peorder list
            return root
        return helper()

# 106. Construct Binary Tree from Inorder and Postorder Traversal
#
# Given inorder and postorder traversal of a tree, construct the binary tree.
#
# Note:
# You may assume that duplicates do not exist in the tree.
#
# For example, given
#
# inorder = [9,3,15,20,7]
# postorder = [9,15,7,20,3]
# Return the following binary tree:
#
#         3
#       / \
#     9  20
#        / \
#       15   7

    def buildTree_postorder(self, inorder, postorder):
        """
        :type inorder: List[int]
        :type postorder: List[int]
        :rtype: TreeNode
        """
        postorder_index=len(postorder)-1
        inorder_map={val:index for index,val in enumerate(inorder)}
        def helper(left=0,right=len(inorder)-1):
            nonlocal postorder_index
            if left>right:
                return None
            root=TreeNode(postorder[postorder_index])
            postorder_index-=1
            # get the root index from the inorder_root map
            # and we again put in helper the left subtree index and the
            # right subtree index.
            split_index=inorder_map[root.val]
            root.right=helper(split_index+1,right)
            root.left=helper(left,split_index-1)
            # We construct left and right tree till the inorder list is none and we pick the order from peorder list
            return root
        return helper()

s=Solution()
print(s.buildTree_postorder(inorder = [9,3,15,20,7],postorder = [9,15,7,20,3]))


