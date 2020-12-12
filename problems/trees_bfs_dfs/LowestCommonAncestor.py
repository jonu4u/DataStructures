# 236. Lowest Common Ancestor of a Binary Tree
# Given a binary tree, find the lowest common ancestor (LCA) of two given nodes in the tree.
#
# According to the definition of LCA on Wikipedia: “The lowest common ancestor is defined between two nodes p and q as the lowest node in T that has both p and q as descendants (where we allow a node to be a descendant of itself).”
#
#
#
# Example 1:
#
#
# Input: root = [3,5,1,6,2,0,8,null,null,7,4], p = 5, q = 1
# Output: 3
# Explanation: The LCA of nodes 5 and 1 is 3.
# Example 2:
#
#
# Input: root = [3,5,1,6,2,0,8,null,null,7,4], p = 5, q = 4
# Output: 5
# Explanation: The LCA of nodes 5 and 4 is 5, since a node can be a descendant of itself according to the LCA definition.
# Example 3:
#
# Input: root = [1,2], p = 1, q = 2
# Output: 1
# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution(object):

    def lowestCommonAncestor_naive(self, root, p, q):
        """
        :type root: TreeNode
        :type p: TreeNode
        :type q: TreeNode
        :rtype: TreeNode
        """
        parent_p,node_p=self.pre_order(root,p,[])
        # if q is child of p
        root_q,node_q=self.pre_order(node_p,q,[])
        if root_q:
            return node_p
        #if q is child of p's parent
        root_q,node_q=self.pre_order(parent_p,q,[])
        if root_q:
            return parent_p
        # We set p as p's parent and check if q exists as it's child recursively
        # until we find q
        return self.lowestCommonAncestor_naive(root,parent_p.val,q)


    def pre_order(self, root, value, list1):
        if not root:
            return
        if root.val==value:
            list1.extend([root, root])
            return (list1[0], list1[1])
        if root.left and root.left.val==value:
            list1.extend([root, root.left])
            return (list1[0], list1[1])
        elif root.right and root.right.val==value:
            list1.extend([root, root.right])
            return (list1[0], list1[1])
        self.pre_order(root.left, value, list1)
        if len(list1)>0:
            return (list1[0], list1[1])
        self.pre_order(root.right, value, list1)
        if len(list1)>0:
            return (list1[0], list1[1])
        return (None,None)


s=Solution()
n1=TreeNode(3)
n2=TreeNode(5)
n3=TreeNode(1)
n4=TreeNode(6)
n5=TreeNode(2)
n6=TreeNode(0)
n7=TreeNode(8)
n8=TreeNode(7)
n9=TreeNode(4)
n1.left=n2
n1.right=n3
n2.left=n4
n2.right=n5
n5.left=n8
n5.right=n9
n3.left=n6
n3.right=n7
print(s.lowestCommonAncestor_naive(n1,7,3).val)