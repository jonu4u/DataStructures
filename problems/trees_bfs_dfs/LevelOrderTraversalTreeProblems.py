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
    def zigzagLevelOrder(self, root):
        """
        :type root: TreeNode
        :rtype: List[List[int]]
        """
        if not root:
            return []
        q=deque()
        q.append(root)
        q.append(None)
        out=[]
        ctr=0
        inner=[]
        while q:
            curr=q.popleft()
            if not curr and len(q)==0:
                out.append(inner[:])
                break
            elif not curr:
                q.append(None)
                out.append(inner[:])
                inner=[]
                ctr+=1
                continue
            if ctr%2==0:
                inner.append(curr.val)
            else:
                inner.insert(0,curr.val)

            if curr.left:
                q.append(curr.left)
            if curr.right:
                q.append(curr.right)

        return out

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