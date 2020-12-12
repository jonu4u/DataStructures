# 426. Convert Binary Search Tree to Sorted Doubly Linked List
#
# Convert a Binary Search Tree to a sorted Circular Doubly-Linked List in place.
#
# You can think of the left and right pointers as synonymous to the predecessor and successor pointers in a doubly-linked list. For a circular doubly linked list, the predecessor of the first element is the last element, and the successor of the last element is the first element.
#
# We want to do the transformation in place. After the transformation, the left pointer of the tree node should point to its predecessor, and the right pointer should point to its successor. You should return the pointer to the smallest element of the linked list.
#
#
#
# Example 1:
# Input: root = [4,2,5,1,3]
# Output: [1,2,3,4,5]
#
# Explanation: The figure below shows the transformed BST. The solid line indicates the successor relationship, while the dashed line means the predecessor relationship.
#
# Example 2:
#
# Input: root = [2,1,3]
# Output: [1,2,3]
# Example 3:
#
# Input: root = []
# Output: []
# Explanation: Input is an empty tree. Output is also an empty Linked List.
# Example 4:
#
# Input: root = [1]
# Output: [1]
#
#
# Constraints:
#
# -1000 <= Node.val <= 1000
# Node.left.val < Node.val < Node.right.val
# All values of Node.val are unique.
# 0 <= Number of Nodes <= 2000
# Definition for a Node.
from collections import OrderedDict
class Node(object):
    def __init__(self, val, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution(object):
    def treeToDoublyList(self, root):
        """
        :type root: Node
        :rtype: Node
        """
        node_order_map=OrderedDict()
        self.inorder_dfs(root,node_order_map)
        key_list=list(node_order_map.keys())
        current=node_order_map.get(key_list[0])
        for key in key_list[1:]:
               elem=node_order_map.get(key)
               current.right=elem
               elem.left=current
               current=current.right
        head=node_order_map.get(key_list[0])
        current.right=head
        head.left=current
        return head


    def inorder_dfs(self,root,order_map):
        if not root: return
        self.inorder_dfs(root.left,order_map)
        order_map[root.val]=root
        self.inorder_dfs(root.right,order_map)

s=Solution()
n1=Node(1)
n2=Node(2)
n3=Node(3)
n4=Node(4)
n5=Node(5)
n2.left=n1
n2.right=n3
n4.left=n2
n4.right=n5
s.treeToDoublyList(n4)