# 979. Distribute Coins in Binary Tree
#
# Given the root of a binary tree with N nodes, each node in the tree has node.val coins, and there are N coins total.
#
# In one move, we may choose two adjacent nodes and move one coin from one node to another.  (The move may be from parent to child, or from child to parent.)
#
# Return the number of moves required to make every node have exactly one coin.
#
#
#
# Example 1:
#
#
#
# Input: [3,0,0]
# Output: 2
# Explanation: From the root of the tree, we move one coin to its left child, and one coin to its right child.
# Example 2:
#
#
#
# Input: [0,3,0]
# Output: 3
# Explanation: From the left child of the root, we move two coins to the root [taking two moves].  Then, we move one coin from the root of the tree to the right child.
# Example 3:
#
#
#
# Input: [1,0,2]
# Output: 2
# Example 4:
#
#
#
# Input: [1,0,0,null,3]
# Output: 4
#
#
# Note:
#
# 1<= N <= 100
# 0 <= node.val <= N
# Accepted
# 48,903
# Submissions
# 70,692
class Solution(object):
    def distributeCoins(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        return self.dfs(root,0)

    def dfs(self,root,ctr):
        if not root:return ctr
        # take the return value of ctr as ctr is midifiedinside recursion
        # If it was a list the list already contained elements from inside but for intwe have to return value
        ctr=self.dfs(root.left,ctr)
        ctr=self.dfs(root.right,ctr)
        # Main Logic if any node value is graeter than 1 transfer coins to paret till count in node is 1
        #     and if less than 1 then transfer coins from parent to node.
        if root.left and root.left.val>1:
            ctr=ctr+root.left.val-1
            root.val=root.val+root.left.val-1
        elif root.left and root.left.val<=0:
            ctr+=1-root.left.val
            root.val=root.val-(1-root.left.val)

        if root.right and root.right.val>1:
            ctr=ctr+root.right.val-1
            root.val=root.val +root.right.val-1
        elif root.right and root.right.val<=0:
            ctr+=1-root.right.val
            root.val=root.val-(1-root.right.val)
        return ctr