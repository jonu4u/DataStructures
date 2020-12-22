# 304. Range Sum Query 2D - Immutable
#
# Given a 2D matrix matrix, find the sum of the elements inside the rectangle defined by its upper left corner (row1, col1) and lower right corner (row2, col2).
#
# Range Sum Query 2D
# The above rectangle (with the red border) is defined by (row1, col1) = (2, 1) and (row2, col2) = (4, 3), which contains sum = 8.
#
# Example:
# Given matrix = [
#     [3, 0, 1, 4, 2],
#     [5, 6, 3, 2, 1],
#     [1, 2, 0, 1, 5],
#     [4, 1, 0, 1, 7],
#     [1, 0, 3, 0, 5]
# ]
#
# sumRegion(2, 1, 4, 3) -> 8
# sumRegion(1, 1, 2, 2) -> 11
# sumRegion(1, 2, 2, 4) -> 12
# Note:
# You may assume that the matrix does not change.
# There are many calls to sumRegion function.
# You may assume that row1 ≤ row2 and col1 ≤ col2.
class NumMatrix(object):

    def __init__(self, matrix):
        """
        :type matrix: List[List[int]]
        """
        if len(matrix)==0 or len(matrix[0])==0:
            return
        self.matrix=matrix
        rows=len(matrix)
        cols=len(matrix[0])
        # Prepopulating matrix with cumulative sum in each row.NoneSo row(i)=row(i-1)+value at row i
        self.memo=[[None for i in range(0,cols+1)] for i in range(0,rows+1)]
        for row in range(0,rows):
            self.memo[row][0]=self.matrix[row][0]
            for col in range(1,cols):
                self.memo[row][col]=self.memo[row][col-1]+self.matrix[row][col]


    def sumRegion(self, row1, col1, row2, col2):
        """
        :type row1: int
        :type col1: int
        :type row2: int
        :type col2: int
        :rtype: int
        """
        sum=0
        for row in range(row1,row2+1):
            # When the col1 is 0 no need to subtract take entire value of col2
            # for that row.
            if col1==0:
                sum+=self.memo[row][col2]
            # Subtract col1-1 from col2 to get col2 to col1 value
            else:
                sum+=self.memo[row][col2]-self.memo[row][col1-1]
        return sum



# Your NumMatrix object will be instantiated and called as such:
# obj = NumMatrix(matrix)
# param_1 = obj.sumRegion(row1,col1,row2,col2)
