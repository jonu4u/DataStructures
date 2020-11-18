# 366. Find Leaves of Binary Tree
# Given a binary tree, collect a tree's nodes as if you were doing this: Collect and remove all leaves, repeat until the tree is empty.
#
#
#
# Example:
#
# Input: [1,2,3,4,5]
#
# 1
# / \
#     2   3
# / \
#     4   5
#
# Output: [[4,5,3],[2],[1]]
#
#
# Explanation:
#
# 1. Removing the leaves [4,5,3] would result in this tree:
#
# 1
# /
# 2
#
#
# 2. Now removing the leaf [2] would result in this tree:
#
# 1
#
#
# 3. Now removing the leaf [1] would result in the empty tree:
#
# []
# [[3,5,4],[2],[1]], [[3,4,5],[2],[1]], etc, are also consider correct answers since per each level it doesn't matter the order on which elements are returned.

# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution(object):
    def findLeaves(self, root):
        """
        :type root: TreeNode
        :rtype: List[List[int]]
        """
        list2=[]
        current=root
        # Until the tree is none we iterate and putin list
        while current:
            leaf_list,modified_root=self.find_and_remove_leaves(current,[])
            list2.append([x.val for x in leaf_list])
            current=modified_root
        return list2

# IN TREE ALWAYS REMEBER TO MATCH NODE WITH NODE INSTEAD OF VALUE IF TREE CONTAINS DUPLICATES
    def find_and_remove_leaves(self,root,list1):
        if not root:return
        # If the node doesn't have any child it's a leaf node
        if not root.left and not root.right:
            list1.append(root)
        self.find_and_remove_leaves(root.left,list1)
        self.find_and_remove_leaves(root.right,list1)
        # Once we find the leaf node we remove that from parent
        # and return the modified tree
        if root.left and root.left in list1:
            root.left=None
        if root.right and root.right in list1:
            root.right=None
        if root in list1:
            root=None
        return (list1,root)
s=Solution()
n1=TreeNode(1)
n2=TreeNode(1)
n3=TreeNode(1)
n4=TreeNode(1)
n5=TreeNode(1)
n6=TreeNode(1)
n7=TreeNode(1)
n8=TreeNode(1)
n9=TreeNode(9)
n10=TreeNode(10)
n11=TreeNode(11)
n12=TreeNode(12)
n1.left=n2
n1.right=n9
n2.left=n3
n2.right=n10
n3.left=n4
n9.left=n5
n5.left=n11
n11.left=n12
n9.right=n8
n8.left=n6
n8.right=n7
print(s.findLeaves(n1))

