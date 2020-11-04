# 103. Binary Tree Zigzag Level Order Traversal
# Given a binary tree, return the zigzag level order traversal of its nodes' values. (ie, from left to right, then right to left for the next level and alternate between).
#
# For example:
# Given binary tree [3,9,20,null,null,15,7],
#     3
#    / \
#   9  20
#      / \
#     15   7
# return its zigzag level order traversal as:
# [
#     [3],
#     [9,20],
#     [7,15]
# ]
from collections import deque
# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class LevelOrderNormal(object):
    def levelOrder(self, root):
        """
        :type root: TreeNode
        :rtype: List[List[int]]
        """
        output={}
        if root is None:
            return output
        q=deque([root])
        # peek returns first element from q.So till q is not null
        while len(q)>0 and q[0] is not None:
            element_peeked=q.popleft()
            height=self.height_of_node(root,element_peeked)
            if output.get(height) is not None:
                output.get(height).append(element_peeked.val)
            else:
                output[height]=[element_peeked.val]
            # left=left of element peeked and right is right
            left=element_peeked.left
            right=element_peeked.right
            # if not none then put in q and loop
            if left is not None:
                q.append(left)
            if right is not None:
                q.append(right)
        return output.values()

    def __getHeight__(self,root, node, level):
        if (root == None):
            return 0

        if (root == node) :
            return level

        downlevel = self.__getHeight__(root.left,
                                       node, level + 1)
        if (downlevel != 0) :
            return downlevel

        downlevel = self.__getHeight__(root.right,
                                       node, level + 1)
        return downlevel


    def height_of_node(self,root, data) :
        return self.__getHeight__(root, data, 1)

# 107. Binary Tree Level Order Traversal II
# Given a binary tree, return the bottom-up level order traversal of its nodes' values. (ie, from left to right, level by level from leaf to root).
#
# For example:
# Given binary tree [3,9,20,null,null,15,7],
#       3
#      / \
#     9  20
#        / \
#       15   7
# return its bottom-up level order traversal as:
# [
#     [15,7],
#     [9,20],
#     [3]
# ]
# This can be easily done by similar algo as above by just reversing the list,
# let's try something else
class LevelOrderReverse(object):
    def levelOrderBottom(self, root):
        """
        :type root: TreeNode
        :rtype: List[List[int]]
        """
        output=[]
        if root is None:
            return output
        # None marks end of level in the q. For root None is after root.
        q=deque([root,None])
        while len(q)>1 :
        # take the left element as current element from q
            current_elem=q.popleft()
        # This list will keep all elements of a level together
            list=[]
        # Until the current element reaches None , it means that level is not exhausted and we add the child nodes of left and right
        # by popping each element
            while current_elem is not None:
                list.append(current_elem.val)
                if current_elem.left is not None:
                    q.append(current_elem.left)
                if current_elem.right is not None:
                    q.append(current_elem.right)
                # Move the current element to next item of q
                current_elem=q.popleft()
        #     Once we come out of th above while a level has ended.So we add the ist in the outer list
        # and append the None marker to mark end of this level
            output.append(list)
            q.append(None)
        # reverse the list to return level order bottom
        output.reverse()
        return output

    def __getHeight__(self,root, node, level):
        if (root == None):
            return 0

        if (root == node) :
            return level

        downlevel = self.__getHeight__(root.left,
                                       node, level + 1)
        if (downlevel != 0) :
            return downlevel

        downlevel = self.__getHeight__(root.right,
                                       node, level + 1)
        return downlevel


    def height_of_node(self,root, data) :
        return self.__getHeight__(root, data, 1)