# 257. Binary Tree Paths
#
# Given a binary tree, return all root-to-leaf paths.
#
# Note: A leaf is a node with no children.
#
# Example:
#
# Input:
#
#      1
#     / \
#    2   3
#     \
#      5
#
# Output: ["1->2->5", "1->3"]
#
# Explanation: All root-to-leaf paths are: 1->2->5, 1->3

# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution(object):
    def binaryTreePaths(self, root):
        """
        :type root: TreeNode
        :rtype: List[str]
        """
        if not root:
            return root
        return self.traversal(root,[],[])

    def traversal(self,root,list1,list2):
        # Add the element in the secondary list
        list2.append(root.val)
        # if the element doesn't have any child it's a leaf node
        if not root.left and not root.right:
            # append the inner list to the return list
            list1.append(self.create_string(list2))
            # remove the last element from the inner list, as we go up in recursion
            size=len(list2)
            list2.pop(size-1)
            return list1
        # if we have only right child, we traverse on the left child
        if not root.left:
            self.traversal(root.right,list1,list2)
            # once we traverse it we remove the last element from inner list
            size=len(list2)
            list2.pop(size-1)
            return list1
        # if we have only left child, we traverse on the right child
        if not root.right:
            self.traversal(root.left,list1,list2)
            size=len(list2)
            # once we traverse it we remove the last element from inner list
            list2.pop(size-1)
            return list1
        # If we have both left and right we do recursion on left and right
        self.traversal(root.left,list1,list2)
        self.traversal(root.right,list1,list2)
        # Remove the node that we just traversed wjhich is last element of innner list
        size=len(list2)
        list2.pop(size-1)
        return list1

    def create_string(self,list1):
        sum=str(list1[0])
        index=1
        size=len(list1)
        while index<size:
            sum=sum+"->"+str(list1[index])
            index+=1
        return sum

s=Solution()
n1=TreeNode(1)
n2=TreeNode(2)
n3=TreeNode(1)
n4=TreeNode(4)
n5=TreeNode(5)
n6=TreeNode(6)
n7=TreeNode(7)
n8=TreeNode(7)

n1.left=n2
n1.right=n3
n3.left=n4
n3.right=n5
n5.right=n6
n6.left=n7
n7.right=n8
s.binaryTreePaths(n1)