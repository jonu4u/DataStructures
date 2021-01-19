# 655. Print Binary Tree
#
# Print a binary tree in an m*n 2D string array following these rules:
#
# The row number m should be equal to the height of the given binary tree.
# The column number n should always be an odd number.
# The root node's value (in string format) should be put in the exactly middle of the first row it can be put. The column and the row where the root node belongs will separate the rest space into two parts (left-bottom part and right-bottom part). You should print the left subtree in the left-bottom part and print the right subtree in the right-bottom part. The left-bottom part and the right-bottom part should have the same size. Even if one subtree is none while the other is not, you don't need to print anything for the none subtree but still need to leave the space as large as that for the other subtree. However, if two subtrees are none, then you don't need to leave space for both of them.
# Each unused space should contain an empty string "".
# Print the subtrees following the same rules.
# Example 1:
# Input:
# 1
# /
# 2
# Output:
# [["", "1", ""],
#  ["2", "", ""]]
# Example 2:
# Input:
# 1
# / \
#     2   3
# \
# 4
# Output:
# [["", "", "", "1", "", "", ""],
#  ["", "2", "", "", "", "3", ""],
#  ["", "", "4", "", "", "", ""]]
# Example 3:
# Input:
# 1
# / \
#     2   5
# /
# 3
# /
# 4
# Output:
#
# [["",  "",  "", "",  "", "", "", "1", "",  "",  "",  "",  "", "", ""]
#  ["",  "",  "", "2", "", "", "", "",  "",  "",  "",  "5", "", "", ""]
#  ["",  "3", "", "",  "", "", "", "",  "",  "",  "",  "",  "", "", ""]
#  ["4", "",  "", "",  "", "", "", "",  "",  "",  "",  "",  "", "", ""]]
# Note: The height of binary tree is in the range of [1, 10].

# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
# O(h.2^h) Time and space
class Solution(object):
    def printTree(self, root):
        """
        :type root: TreeNode
        :rtype: List[List[str]]
        """
        height=self.getHeight(root)
        res=[["" for col in range(2**height-1)] for row in range(height)]
        self.print_arr(res,root,0,0,len(res[0]))
        return res

    def print_arr(self,res,root,row,left_idx,right_idx):
        if not root: return
        mid=(left_idx+right_idx)//2
        res[row][mid]=str(root.val)
        self.print_arr(res,root.left,row+1,left_idx,mid-1)
        self.print_arr(res,root.right,row+1,mid+1,right_idx)
        return



    def getHeight(self,root):
        if not root: return 0
        return max(self.getHeight(root.left),self.getHeight(root.right))+1