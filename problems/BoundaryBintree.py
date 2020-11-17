# 545. Boundary of Binary Tree
#
# A binary tree boundary is the set of nodes (no duplicates) denoting the union of the left boundary, leaves, and right boundary.
#
# The left boundary is the set of nodes on the path from the root to the left-most node. The right boundary is the set of nodes on the path from the root to the right-most node.
#
# The left-most node is the leaf node you reach when you always travel to the left subtree if it exists and the right subtree if it doesn't. The right-most node is defined in the same way except with left and right exchanged. Note that the root may be the left-most and/or right-most node.
#
# Given the root of a binary tree, return the values of its boundary in a counter-clockwise direction starting from the root.
#
#
#
# Example 1:
#
#
# Input: root = [1,null,2,3,4]
# Output: [1,3,4,2]
# Explanation:
# The left boundary is the nodes [1,2,3].
# The right boundary is the nodes [1,2,4].
# The leaves are nodes [3,4].
# Unioning the sets together gives [1,2,3,4], which is [1,3,4,2] in counter-clockwise order.
# Example 2:
#
#
# Input: root = [1,2,3,4,5,6,null,null,null,7,8,9,10]
# Output: [1,2,4,7,8,9,10,6,3]
# Explanation:
# The left boundary are node 1,2,4. (4 is the left-most node according to definition)
# The left boundary is nodes [1,2,4].
# The right boundary is nodes [1,3,6,10].
# The leaves are nodes [4,7,8,9,10].
# Unioning the sets together gives [1,2,3,4,6,7,8,9,10], which is [1,2,4,7,8,9,10,6,3] in counter-clockwise order.
#
#
# Constraints:
#
# The number of nodes in the tree is in the range [0, 104].
# -1000 <= Node.val <= 1000
# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution(object):
    def boundaryOfBinaryTree(self, root):
        """
        :type root: TreeNode
        :rtype: List[int]
        """
        if not root:
            return []
        if not root.left and not root.right:
            return [root.val]
        left_list=self.create_left_list(root,[])
        right_list=self.create_right_list(root,[])
        right_list.reverse()
        leaf_list=self.pre_order(root,[])
        final_list=[root.val]+left_list+leaf_list+right_list
        return final_list

    def create_right_list(self,root,list1):
        current=root
        next_right=current.right
        while current and next_right:
            if not next_right.left and not next_right.right:
                break
            list1.append(next_right.val)
            current=next_right
            next_right=current.right if current.right else current.left
        return list1

    def create_left_list(self,root,list1):
        current=root
        next_left=current.left
        while current and  next_left:
            if not next_left.left and not next_left.right:
                break
            list1.append(next_left.val)
            current=current.left
            next_left=current.left if current.left else current.right
        return list1


    def pre_order(self,root,leaf_list):
        if not root:return
        if not root.left and not root.right:
            leaf_list.append(root.val)
        self.pre_order(root.left,leaf_list)
        self.pre_order(root.right,leaf_list)
        return leaf_list



s=Solution()
n1=TreeNode(1)
n2=TreeNode(2)
n3=TreeNode(3)
n4=TreeNode(4)
n5=TreeNode(5)
n6=TreeNode(6)
n7=TreeNode(7)
n8=TreeNode(8)
n9=TreeNode(9)
n10=TreeNode(10)
n1.left=n2
n1.right=n3
n2.left=n4
n2.right=n5
n3.left=n6
n6.left=n9
n6.right=n10
n5.left=n7
n5.right=n8
print(s.boundaryOfBinaryTree(n1))

# n1=TreeNode(1)
# n2=TreeNode(2)
# n3=TreeNode(3)
# n4=TreeNode(4)
# n1.right=n2
# n2.left=n3
# n2.right=n4
#
# print(s.boundaryOfBinaryTree(n1))

n1=TreeNode(1)
n2=TreeNode(2)
n3=TreeNode(3)
n4=TreeNode(4)
n5=TreeNode(5)
n6=TreeNode(6)
n7=TreeNode(7)
n8=TreeNode(8)
n9=TreeNode(9)
n1.left=n2
n1.right=n9
n2.left=n3
n3.left=n4
n9.left=n5
n9.right=n8
n8.left=n6
n8.right=n7

print(s.boundaryOfBinaryTree(n1))