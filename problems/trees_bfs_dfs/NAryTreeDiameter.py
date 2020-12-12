# 1522. Diameter of N-Ary Tree
#
# Given a root of an N-ary tree, you need to compute the length of the diameter of the tree.
#
# The diameter of an N-ary tree is the length of the longest path between any two nodes in the tree. This path may or may not pass through the root.
#
# (Nary-Tree input serialization is represented in their level order traversal, each group of children is separated by the null value.)
#
#
#
# Example 1:
#
#               1
#            /  /  \
#           3   2   4
#          / \
#         5   6
#
# Input: root = [1,null,3,2,4,null,5,6]
# Output: 3
# Explanation: Diameter is shown in red color.
# Example 2:
#                    1
#                    /
#                   2
#                  / \
#                3    4
#               /       \
#              5         6
#
#
# Input: root = [1,null,2,null,3,4,null,5,null,6]
# Output: 4
#
#
#
# Constraints:
#
# The depth of the n-ary tree is less than or equal to 1000.
# The total number of nodes is between [0, 10^4].

# Definition for a Node.
class Node(object):
    def __init__(self, val=None, children=None):
        self.val = val
        self.children = children if children is not None else []

from collections import deque
class Solution(object):
    def __init__(self):
        self.ans=0
        self.sum=0
        # self.node_length=float('-inf')
    def diameter(self, root):
        """
        :type root: 'Node'
        :rtype: int
        """
        if not root:
            return 0
        self.ans=float('-inf')
        self.dfs(root)
        return self.ans

    def dfs(self,root):
        if not root: return 0
        q=deque()
        for child in root.children:
            q.append(self.dfs(child))
            if len(q)>2:
                q.popleft()

        l1,l2=0,0
        if len(q)>0:
            l1=q.popleft()
        if len(q)>0:
            l2=q.popleft()
        self.ans=max(self.ans,l1+l2)
        return max(l1,l2)+1

s=Solution()
n1=Node(1,[])
n2=Node(2,[])
n3=Node(3,[])
n4=Node(4,[])
n5=Node(5,[])
n6=Node(6,[])
n1.children=[n2]
n2.children=[n3,n4]
n3.children=[n5]
n4.children=[n6]
print(s.diameter(n1))