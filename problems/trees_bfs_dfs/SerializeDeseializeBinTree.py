# 297. Serialize and Deserialize Binary Tree
#
# Serialization is the process of converting a data structure or object into a sequence of bits so that it can be stored in a file or memory buffer, or transmitted across a network connection link to be reconstructed later in the same or another computer environment.
#
# Design an algorithm to serialize and deserialize a binary tree. There is no restriction on how your serialization/deserialization algorithm should work. You just need to ensure that a binary tree can be serialized to a string and this string can be deserialized to the original tree structure.
#
# Clarification: The input/output format is the same as how LeetCode serializes a binary tree. You do not necessarily need to follow this format, so please be creative and come up with different approaches yourself.
#
# Input: root = [1,2,3,null,null,4,5]
# Output: [1,2,3,null,null,4,5]
# Example 2:
#
# Input: root = []
# Output: []
# Example 3:
#
# Input: root = [1]
# Output: [1]
# Example 4:
#
# Input: root = [1,2]
# Output: [1,2]
# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

# THE TRICK IS USE SAME TRAVERSAL FOR SERIALIZE AND DESERIALIZE
class Codec:

    def serialize(self, root):
        """Encodes a tree to a single string.

        :type root: TreeNode
        :rtype: str
        """
        return self.serialize_preorder(root)


    def deserialize(self, data):
        """Decodes your encoded data to tree.

        :type data: str
        :rtype: TreeNode
        """
        # We create a list from the string data
        list_node=data.split(",")
        return self.deserialize_preorder(list_node)


    def serialize_preorder(self,root,string):
        # If there is no element return String 'None'
        if not root:
            string+='None'
            return string
        # Idea is to create a comma sepated string list of node.vals by preorder
        string+=str(root.val)+','
        string=self.serialize_preorder(root.left,string)
        string=self.serialize_preorder(root.right,string)
        return string

    def deserialize_preorder(self,list_node):
        # here we pick each element from the list of node ceate the tree again
        if list_node[0]=='None':
            list_node.pop(0)
            return None
        root=list_node[0]
        list_node.pop(0)
        # The moment we create a node we remove that from list.
        # The trick is the order used for serializing we should use same order for desrializing also
        root.left=self.deserialize_preorder(list_node)
        root.right=self.deserialize_preorder(list_node)
        return root

# Your Codec object will be instantiated and called as such:
# ser = Codec()
# deser = Codec()
# ans = deser.deserialize(ser.serialize(root))