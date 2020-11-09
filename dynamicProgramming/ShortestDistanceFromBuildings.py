# 317. Shortest Distance from All Buildings
#
# You want to build a house on an empty land which reaches all buildings in the shortest amount of distance. You can only move up, down, left and right. You are given a 2D grid of values 0, 1 or 2, where:
#
# Each 0 marks an empty land which you can pass by freely.
# Each 1 marks a building which you cannot pass through.
# Each 2 marks an obstacle which you cannot pass through.
# Example:
#
# Input: [[1,0,2,0,1],[0,0,0,0,0],[0,0,1,0,0]]
#
# 1 - 0 - 2 - 0 - 1
# |   |   |   |   |
# 0 - 0 - 0 - 0 - 0
# |   |   |   |   |
# 0 - 0 - 1 - 0 - 0
#
# Output: 7
#
# Explanation: Given three buildings at (0,0), (0,4), (2,2), and an obstacle at (0,2),
# the point (1,2) is an ideal empty land to build a house, as the total
# travel distance of 3+3+1=7 is minimal. So return 7.
# Note:
# There will be at least one building. If it is not possible to build such house according to the above rules, return -1.


class Solution(object):
    # This solution gives time limit exceeded
    def shortestDistance_naive_backtracking_recursion(self, grid):
        """
        :type grid: List[List[int]]
        :rtype: int
        """
        # Iterate thru the grid and put locations of buildings and lands
        if len(grid)==0 or len(grid[0])==0:
            return 0
        land_positions=[]
        building_positions=[]
        min_distance=float('inf')

        row_len=len(grid)
        col_len=len(grid[0])
        boolean_grid=[[False for col in range(0,col_len)] for row in range(0,row_len)]
        for row in range(0,row_len):
            for col in range(0,col_len):
                if grid[row][col]==1:
                    building_positions.append((row,col))
                if grid[row][col]==0:
                    land_positions.append((row,col))
        for land in land_positions:
            sum=0
            is_visited=boolean_grid[:]
            for building in building_positions:
                distance=self.shortest_distance_two_points(grid,land[0],land[1],building[0],building[1],is_visited)
                if distance==float('inf'):
                    sum=float('inf')
                    break
                sum=sum+distance
                if sum>=min_distance:
                    break
            min_distance=min(min_distance,sum)
        if min_distance==float('inf'):
            min_distance=-1
        return min_distance

    # We'll try backtracking to find shortest path from each land to a building.' \
    #   Sum up all the paths and see which position (land) gives min distance

    # So here we break the entire problem into shortest path of each point to each builing and extend it for the whole lands

    #  is_visited is a 2D matrix having same number of rows and cols like given grid.When we visit a coordinated we mark
    # that point in is_visited as true
    def shortest_distance_two_points(self,grid,source_x,source_y,dest_x,dest_y,is_visited):
        # Base case when we reach dest
        if source_x==dest_x and source_y==dest_y:
            return 0
        row_len=len(grid)
        col_len=len(grid[0])
        # So here we check if the source coordnates are valid and if the coordinate is already not visited.
        # Also we can only move on grid value 0
        if (source_x<0 or source_y<0 or source_x>=row_len or source_y>=col_len or is_visited[source_x][source_y] or grid[source_x][source_y]!=0):
         # if a path is not possible
            return float('inf')

        is_visited[source_x][source_y]=True
        # Now we move right left up and down to find paths
        left=self.shortest_distance_two_points(grid,source_x,source_y-1,dest_x,dest_y,is_visited) +1
        right=self.shortest_distance_two_points(grid,source_x,source_y+1,dest_x,dest_y,is_visited) +1
        up=self.shortest_distance_two_points(grid,source_x-1,source_y,dest_x,dest_y,is_visited) +1
        down=self.shortest_distance_two_points(grid,source_x+1,source_y,dest_x,dest_y,is_visited) +1
        # After we do recursion we come back to the starting point,
        # this is called backtracking. So we mark the point visited again as False
        # so that other paths can visit this point.
        is_visited[source_x][source_y]=False
        # We want to return the min of the up,down,left,right paths
        return min(left,right,up,down)

s=Solution()
# grid=[[1,0,2,0,1],[0,0,0,0,0],[0,0,1,0,0]]
# print(s.shortestDistance_naive_backtracking_recursion(grid))
# grid1=[[1,1],[0,1]]
# print(s.shortestDistance_naive_backtracking_recursion(grid1))
grid2=[[1,1,1,1,1,0],[0,0,0,0,0,1],[0,1,1,0,0,1],[1,0,0,1,0,1],[1,0,1,0,0,1],[1,0,0,0,0,1],[0,1,1,1,1,0]]
print(s.shortestDistance_naive_backtracking_recursion(grid2))


