# 1277. Count Square Submatrices with All Ones
#
# Given a m * n matrix of ones and zeros, return how many square submatrices have all ones.
#
#
#
# Example 1:
#
# Input: matrix =
# [
#     [0,1,1,1],
#     [1,1,1,1],
#     [0,1,1,1]
# ]
# Output: 15
# Explanation:
# There are 10 squares of side 1.
# There are 4 squares of side 2.
# There is  1 square of side 3.
# Total number of squares = 10 + 4 + 1 = 15.
# Example 2:
#
# Input: matrix =
# [
#     [1,0,1],
#     [1,1,0],
#     [1,1,0]
# ]
# Output: 7
# Explanation:
# There are 6 squares of side 1.
# There is 1 square of side 2.
# Total number of squares = 6 + 1 = 7.
#
#
# Constraints:
#
# 1 <= arr.length <= 300
# 1 <= arr[0].length <= 300
# 0 <= arr[i][j] <= 1

# https://leetcode.com/problems/count-square-submatrices-with-all-ones/discuss/643429/Python-DP-Solution-%2B-Thinking-Process-Diagrams-(O(mn)-runtime-O(1)-space)
class Solution(object):
    def countSquares(self, matrix):
        """
        :type matrix: List[List[int]]
        :rtype: int
        """
        if matrix is None or len(matrix[0])==0:
            return 0
        row_len=len(matrix)
        col_len=len(matrix[0])
        ans=0
        for row in range(row_len):
            for col in range(col_len):
                if matrix[row][col]==1:
                    # For the boundary cells whenever we get 1 we sinply add to result
                    if row==0 or col==0:
                        ans+=1
                    else:
                        # For down right cells like (1,1),(2,1) etc which are not in boundary
                        # we take minimum of left, up and up left diagonal +1 to get count of square
                        cell_val=min(matrix[row-1][col],matrix[row][col-1],matrix[row-1][col-1]) +1
                        ans+=cell_val
                        # We update/memoize the matrix cell with the new value
                        # for use in next steps
                        matrix[row][col]=cell_val
        return ans