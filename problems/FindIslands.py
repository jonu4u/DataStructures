# 200. Number of Islands
#
# Given an m x n 2d grid map of '1's (land) and '0's (water), return the number of islands.
#
# An island is surrounded by water and is formed by connecting adjacent lands horizontally or vertically. You may assume all four edges of the grid are all surrounded by water.
#
#
# Example 1:
#
# Input: grid = [
#     ["1","1","1","1","0"],
#     ["1","1","0","1","0"],
#     ["1","1","0","0","0"],
#     ["0","0","0","0","0"]
# ]
# Output: 1
# Example 2:
#
# Input: grid = [
#     ["1","1","0","0","0"],
#     ["1","1","0","0","0"],
#     ["0","0","1","0","0"],
#     ["0","0","0","1","1"]
# ]
# Output: 3
#
#
# Constraints:
#
# m == grid.length
# n == grid[i].length
# 1 <= m, n <= 300
# grid[i][j] is '0' or '1'.

class Solution(object):
    # This works but time limit exceeded
    def numIslands_union_find(self, grid):
        """
        :type grid: List[List[str]]
        :rtype: int
        """
        if grid is None or len(grid[0])==0:
            return 0
        vertices={}
        row_len=len(grid)
        col_len=len(grid[0])
        max_len=max(row_len,col_len)
        for row_index,row in enumerate(grid):
            for col_index,col in enumerate(grid[row_index]):
                if col=="1":
                    # zfill used so that if row=17 and col=1 it should be 1701 so padding on left to help in max length of row or column
                    vertices[str(row_index).zfill(max_len)+str(col_index).zfill(max_len)]=[str(row_index).zfill(max_len)+str(col_index).zfill(max_len)]

        for row_index1,row in enumerate(grid):
            for col_index1,col in enumerate(grid[row_index1]):
                if grid[row_index1][col_index1]=="0":
                    continue
                elem=str(row_index1).zfill(max_len)+str(col_index1).zfill(max_len)
                # Now check neighbours and union if found
                # right neighbour
                if col_index1+1<col_len and grid[row_index1][col_index1+1]=="1":
                    self.union(elem,str(row_index1).zfill(max_len)+str(col_index1+1).zfill(max_len),vertices)
                #left neighbour
                if col_index1-1>0 and grid[row_index1][col_index1-1]=="1":
                    self.union(elem,str(row_index1).zfill(max_len)+str(col_index1-1).zfill(max_len),vertices)
                #up neighbour
                if row_index1-1>0 and grid[row_index1-1][col_index1]=="1":
                    self.union(elem,str(row_index1-1).zfill(max_len)+str(col_index1).zfill(max_len),vertices)
                #down neighbour
                if row_index1+1<row_len and grid[row_index1+1][col_index1]=="1":
                    self.union(elem,str(row_index1+1).zfill(max_len)+str(col_index1).zfill(max_len),vertices)
                if len(vertices)==1:
                    break

        return len(vertices)





    def find(self,value,graph):
        for key,value_list in graph.items():
            if value in value_list:
                return key


    def union(self,value1,value2,graph):
        parent1=self.find(value1,graph)
        parent2=self.find(value2,graph)
        if not parent1 or not parent2 or parent1 == parent2:
            return
        size1=len(graph.get(parent1))
        size2=len(graph.get(parent2))
        if size1>=size2:
            self.combine(parent1,parent2,graph)
        else:
            self.combine(parent2,parent1,graph)

    # Put map 2 in 1
    def combine(self,value1,value2,graph):
        list1=graph.get(value1)
        list1.extend(graph.get(value2))
        graph[value1]=list1
        graph.pop(value2)


    def numIslands_dfs(self, grid):
        """
        :type grid: List[List[str]]
        :rtype: int
        """
        if grid is None or len(grid[0])==0:
            return 0
        number_of_islands=0
        for row_index,row in enumerate(grid):
            for col_index,col in enumerate(grid[row_index]):
                if col=="1":
                    number_of_islands+=1
                    self.combine_islands(row_index,col_index,grid)

        return number_of_islands

    def combine_islands(self,row,col,grid):
        row_len=len(grid)
        col_len=len(grid[0])
        if row>=row_len or row<0 or col>=col_len or col<0 or grid[row][col]=="0":
            return
        grid[row][col]="0"
        self.combine_islands(row+1,col,grid)
        self.combine_islands(row-1,col,grid)
        self.combine_islands(row,col+1,grid)
        self.combine_islands(row,col-1,grid)






s=Solution()
grid1 = [
        ["1","1","0","0","0"],
        ["1","1","0","0","0"],
        ["0","0","1","0","0"],
        ["0","0","0","1","1"]
    ]
print(s.numIslands_dfs(grid1))
grid2 = [
    ["1","1","1","1","0"],
    ["1","1","0","1","0"],
    ["1","1","0","0","0"],
    ["0","0","0","0","0"]
]
print(s.numIslands_dfs(grid2))
grid3=[["1","0","1","1","1"],["1","0","1","0","1"],["1","1","1","0","1"]]
print(s.numIslands_dfs(grid3))

grid4=[["1","0","0","1","1","1","0","1","1","0","0","0","0","0","0","0","0","0","0","0"],
       ["1","0","0","1","1","0","0","1","0","0","0","1","0","1","0","1","0","0","1","0"],
       ["0","0","0","1","1","1","1","0","1","0","1","1","0","0","0","0","1","0","1","0"],
       ["0","0","0","1","1","0","0","1","0","0","0","1","1","1","0","0","1","0","0","1"],
       ["0","0","0","0","0","0","0","1","1","1","0","0","0","0","0","0","0","0","0","0"],
       ["1","0","0","0","0","1","0","1","0","1","1","0","0","0","0","0","0","1","0","1"],
       ["0","0","0","1","0","0","0","1","0","1","0","1","0","1","0","1","0","1","0","1"],
       ["0","0","0","1","0","1","0","0","1","1","0","1","0","1","1","0","1","1","1","0"],
       ["0","0","0","0","1","0","0","1","1","0","0","0","0","1","0","0","0","1","0","1"],
       ["0","0","1","0","0","1","0","0","0","0","0","1","0","0","1","0","0","0","1","0"],
       ["1","0","0","1","0","0","0","0","0","0","0","1","0","0","1","0","1","0","1","0"],
       ["0","1","0","0","0","1","0","1","0","1","1","0","1","1","1","0","1","1","0","0"],
       ["1","1","0","1","0","0","0","0","1","0","0","0","0","0","0","1","0","0","0","1"],
       ["0","1","0","0","1","1","1","0","0","0","1","1","1","1","1","0","1","0","0","0"],
       ["0","0","1","1","1","0","0","0","1","1","0","0","0","1","0","1","0","0","0","0"],
       ["1","0","0","1","0","1","0","0","0","0","1","0","0","0","1","0","1","0","1","1"],
       ["1","0","1","0","0","0","0","0","0","1","0","0","0","1","0","1","0","0","0","0"],
       ["0","1","1","0","0","0","1","1","1","0","1","0","1","0","1","1","1","1","0","0"],
       ["0","1","0","0","0","0","1","1","0","0","1","0","1","0","0","1","0","0","1","1"],
       ["0","0","0","0","0","0","1","1","1","1","0","1","0","0","0","1","1","0","0","0"]]
print(s.numIslands_dfs(grid4))