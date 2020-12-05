# 1314. Matrix Block Sum
#
# Given a m * n matrix mat and an integer K, return a matrix answer where each answer[i][j] is the sum of all elements mat[r][c] for i - K <= r <= i + K, j - K <= c <= j + K, and (r, c) is a valid position in the matrix.
#
#
# Example 1:
#
# Input: mat = [[1,2,3],[4,5,6],[7,8,9]], K = 1
# Output: [[12,21,16],[27,45,33],[24,39,28]]
# Example 2:
#
# Input: mat = [[1,2,3],[4,5,6],[7,8,9]], K = 2
# Output: [[45,45,45],[45,45,45],[45,45,45]]
#
#
# Constraints:
#
# m == mat.length
# n == mat[i].length
# 1 <= m, n, K <= 100
# 1 <= mat[i][j] <= 100
class Solution(object):
    def matrixBlockSum(self, mat, K):
        """
        :type mat: List[List[int]]
        :type K: int
        :rtype: List[List[int]]
        """
        row_len=len(mat)
        col_len=len(mat[0])
        ans=[[0 for col in range(0,col_len)] for row in range(0,row_len)]

        def sum(row,col,total,i,j,is_visited):
            if row<0 or row>=row_len or row<i-K or row>i+K or col<0 or col>=col_len or col<j-K or col>j+K or is_visited[row][col]:
                return 0
            is_visited[row][col]=True
            total+=mat[row][col]+ sum(row-1,col,total,i,j,is_visited)+ sum(row+1,col,total,i,j,is_visited)+ sum(row,col-1,total,i,j,is_visited)+ sum(row,col+1,total,i,j,is_visited)
            return total

        for row in range(row_len):
            for col in range(col_len):
                is_visited=[[False for i in range(0,col_len)] for i in range(0,row_len)]
                ans[row][col]=sum(row,col,0,row,col,is_visited)
        return ans

#     dp[i][j] = sum of the rectangle starting at (0,0) top left and ending at (i,j) bottom right
# once this is done( in O(nm)) using this recurrence relation:
#
# dp[i][j] = 0
# "move up one row and add that rectangle"
# dp[i][j] += dp[i-1][j]
#
# "move left one column and add that rectangle"
# dp[i][j] += dp[i][j-1]
#
# "move left and up , and remove that rectangle as its been added multiple times (two)"
# dp[i][j] += dp[i-1][j-1]
#
# "add the value at that cell"
# dp[i][j] += mat[i][j]
#
# we be using it (dp) to compute area of random rectangles starting at some point and ending at some point

    # COME BACK LATER DIDN'T UNDERSTOOD IT'
    def matrixBlockSum_DP(self, mat, K):
        row_len=len(mat)
        col_len=len(mat[0])
        dp=[[0 for col in range(0,col_len)] for row in range(0,row_len)]
        n,m = len(mat), len(mat[0])
        for i in range(n):
            for j in range(m):
                dp[i][j] = mat[i][j]
                if i-1>=0 and j-1>=0: dp[i][j] -= dp[i-1][j-1]
                if i-1>=0: dp[i][j] += dp[i-1][j]
                if j-1>=0: dp[i][j] += dp[i][j-1]
        return [[self.f(i,j,dp,K) for j in range(m)] for i in range(n)]
    def f(self, i, j,dp, k):
        m,n = len(dp[0]),len(dp)
        di,dj = min(n - 1, i + k), min(m - 1, j + k)
        bi,bj = i - k - 1, min(m - 1, j + k)
        ai,aj = i - k - 1, j - k - 1
        ci,cj = min(n - 1, i + k), j - k - 1
        ret = dp[di][dj]
        if bi >=0:  ret -= dp[bi][bj]
        if cj >=0:  ret -= dp[ci][cj]
        if aj >=0 and ai >=0: ret += dp[ai][aj]
        return ret


s=Solution()
print(s.matrixBlockSum(mat = [[1,2,3],[4,5,6],[7,8,9]], K = 1))
print(s.matrixBlockSum(mat = [[1,2,3],[4,5,6],[7,8,9]], K = 2))

print(s.matrixBlockSum_memo(mat = [[1,2,3],[4,5,6],[7,8,9]], K = 1))
print(s.matrixBlockSum_memo(mat = [[1,2,3],[4,5,6],[7,8,9]], K = 2))

