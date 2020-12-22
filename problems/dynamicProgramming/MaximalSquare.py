# 221. Maximal Square:
# https://leetcode.com/problems/maximal-square/
#
# Given an m x n binary matrix filled with 0's and 1's, find the largest square containing only 1's and return its area.
#
#
#
# Example 1:
#
#
# Input: matrix = [["1","0","1","0","0"],["1","0","1","1","1"],["1","1","1","1","1"],["1","0","0","1","0"]]
# Output: 4
# Example 2:
#
#
# Input: matrix = [["0","1"],["1","0"]]
# Output: 1
# Example 3:
#
# Input: matrix = [["0"]]
# Output: 0
#
#
# Constraints:
#
# m == matrix.length
# n == matrix[i].length
# 1 <= m, n <= 300
# matrix[i][j] is '0' or '1'.
class Solution(object):
    # https://leetcode.com/problems/maximal-square/solution/
    def maximalSquare(self, matrix):
        """
        :type matrix: List[List[str]]
        :rtype: int
        """
        row_len=len(matrix)
        col_len=len(matrix[0])
        max_side=float('-inf')
        # We define a DP array
        dp=[[0 for col in range(col_len)] for row in range(row_len)]
        for row in range(row_len):
            for col in range(col_len):
                if row==0 or col==0:
                    # For boundaries value of DP array is same as matrix array
                    dp[row][col]=int(matrix[row][col])
                    max_side=max(max_side,dp[row][col])
                # Whenever we encounter a 1 we see the adjacent squares and take min of them and add1
                # to it which the size of max square till that 1
                elif matrix[row][col]=="1":
                    dp[row][col]=min(dp[row-1][col],dp[row][col-1],dp[row-1][col-1])+1
                    # The maximum value of the dp cell is the maximum square
                    max_side=max(max_side,dp[row][col])
                # For 0 the dp value is same as matrix value
                else:
                    dp[row][col]=0
        # Return the square with maximum side
        return max_side**2
