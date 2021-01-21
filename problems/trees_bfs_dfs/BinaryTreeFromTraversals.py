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


# Return any binary tree that matches the given preorder and postorder traversals.
#
# Values in the traversals pre and post are distinct positive integers.
#
#
#
# Example 1:
#
# Input: pre = [1,2,4,5,3,6,7], post = [4,5,2,6,7,3,1]
# Output: [1,2,3,4,5,6,7]
#
#
# Note:
#
# 1 <= pre.length == post.length <= 30
# pre[] and post[] are both permutations of 1, 2, ..., pre.length.
# It is guaranteed an answer exists. If there exists multiple answers, you can return any of them.
    def constructFromPrePost(self, pre, post):
        """
        :type pre: List[int]
        :type post: List[int]
        :rtype: TreeNode
        """
        if not pre: return None
        root=TreeNode(pre[0])
        if len(pre)==1: return root

        # if L is number of nodes in left branch
        L=post.index(pre[1])+1
        root.left=self.constructFromPrePost(pre[1:L+1],post[0:L])
        root.right=self.constructFromPrePost(pre[L+1:],post[L:-1])
        return root














s=Solution()
print(s.buildTree_postorder(inorder = [9,3,15,20,7],postorder = [9,15,7,20,3]))


