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

class Solution(object):
    def __init__(self):
        self.dia=0
    def diameter(self, root):
        """
        :type root: 'Node'
        :rtype: int
        """
        def max_depth(node,curr_depth):
            # If no child we return the current depth as max depth
            if not node.children: return curr_depth
            # We define the top 2 height as current depth and 0
            max_dep_1,max_dep_2=curr_depth,0
            for children in node.children:
                depth=max_depth(children,curr_depth+1)
                # if this depth >max_1 then we swap this to max and prev max to max 2
                if depth>max_dep_1:
                    max_dep_1,max_dep_2=depth,max_dep_1
                elif depth>max_dep_2:
                    max_dep_2=depth
            distance=max_dep_1+max_dep_2-2*curr_depth
            self.dia=max(self.dia,distance)
            return max_dep_1
        max_depth(root,0)
        return self.dia

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