# 311. Sparse Matrix Multiplication
#
# Given two sparse matrices A and B, return the result of AB.
#
# You may assume that A's column number is equal to B's row number.
#
# Example:
#
# Input:
#
# A = [
#     [ 1, 0, 0],
#     [-1, 0, 3]
# ]
#
# B = [
#     [ 7, 0, 0 ],
#     [ 0, 0, 0 ],
#     [ 0, 0, 1 ]
# ]
#
# Output:
#
#      |  1 0 0 |   | 7 0 0 |   |  7 0 0 |
# AB = | -1 0 3 | x | 0 0 0 | = | -7 0 3 |
#      | 0 0 1 |
#
#
# Constraints:
#
# 1 <= A.length, B.length <= 100
# 1 <= A[i].length, B[i].length <= 100
# -100 <= A[i][j], B[i][j] <= 100
class Solution(object):
    def multiply(self, A, B):
        """
        :type A: List[List[int]]
        :type B: List[List[int]]
        :rtype: List[List[int]]
        """
        row_A=len(A)
        row_B=len(B)
        col_B=len(B[0])
        c=[[0 for i in range(0,col_B)]for i in range(0,row_A)]
        for row in range(0,len(c)):
            for col in range(0,len(c[0])):
                for k in range(0,row_B):
                    c[row][col]+=A[row][k]*B[k][col]
        return c

    def multiply_fast(self, A, B):
        """
        :type A: List[List[int]]
        :type B: List[List[int]]
        :rtype: List[List[int]]
        """
        row_A=len(A)
        row_B=len(B)
        col_B=len(B[0])
        dictB={}
        for row in range(0,len(B)):
            for col in range(0,len(B[0])):
                if B[row][col]!=0:
                    dictB[str(row)+"-"+str(col)]=B[row][col]
        c=[[0 for i in range(0,col_B)]for i in range(0,row_A)]

        for row in range(0,len(A)):
            for col in range(0,len(A[0])):
                for k in range(0,row_B):
                    if A[row][k]!=0 and (str(k)+"-"+str(col)) in dictB:
                        c[row][col]+=A[row][k]*dictB.get((str(k)+"-"+str(col)))
                        # dictB[str(row+"-"+col)]=B[row][col]
        return c

s=Solution()
A = [
    [ 1, 0, 0],
    [-1, 0, 3]
]

B = [
    [ 7, 0, 0 ],
    [ 0, 0, 0 ],
    [ 0, 0, 1 ]
]
s.multiply_fast(A,B)
