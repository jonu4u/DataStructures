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

import itertools
from collections import deque
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






    # Idea is to compute the shortest distance between each empty land and a building pair.
    #  To do that, we run BFS starting from each building and update the shortest distance to each land that we come across. Once BFS has finished running for all buildings, we simply compute the sum of the distances to all buildings for each land and select the minimum. If this minimum is less than Inf, we know such a land is a possibility and return the minimum we found, otherwise we return -1.

    def shortestDistance(self, grid):
        if not grid:
            return -1
        # create a list of buildings and a set of empty lands for easy search later
        build, land = [], set()
        for x,y in itertools.product(range(len(grid)), range(len(grid[0]))):
            if grid[x][y] == 0:
                land.add((x,y))
            elif grid[x][y] == 1:
                build.append((x,y))
        # if there is no empty land available, we can't proceed further
        if not land:
            return -1

        # create a dictionary where each land's position tuple is a key and its value
        # is a list of length equal to the number of buildings we found above.
        # This list is populated with Inf, to start with, that will be updated by the
        # shortest distance between the land and building pair, found by BFS routine below.
        d = {x: [float('inf')]*len(build) for x in land}

        # BFS for a given building's location
        def BFS(loc):
            x, y = build[loc]
            # (x,y) is building's location on the grid and 0 is the starting distance
            q = deque([(x,y,0)])

            # So here we're checking for each land distance to a building'
            while q:
                x, y, dist = q.popleft()
                for i, j in [(x-1, y), (x+1, y), (x, y-1), (x, y+1)]:
                    # we are interested in only traversing lands whose recorded distance from
                    # current building is more than dist+1. We update their distance and include
                    # these lands in our queue for the next layer, if that's the case
                    if (i,j) in land and d[(i,j)][loc] > dist + 1:
                        d[(i,j)][loc] = dist + 1
                        q.append((i,j,dist+1))

        # run BFS for all buildings to find
        # distance of each land from each building.
        # This is O(lands*buildings) Time complexity
        for loc in range(len(build)):
            BFS(loc)

        # compute the shortest distance to all buildings for each empty land
        min_dist = min(sum(d[x]) for x in land)
        return -1 if min_dist == float('inf') else min_dist


    def shortestDistance_my(self, grid):
        if not grid:
            return -1
        row_len=len(grid)
        col_len=len(grid[0])
        buildings=[]
        lands=set()
        # Find buildings and lands
        for row in range(row_len):
            for col in range(col_len):
                if grid[row][col]==0:
                    lands.add((row,col))
                elif grid[row][col]==1:
                    buildings.append((row,col))
        # If no lands
        if len(lands)==0:
            return -1
        # Create land map to find dist from each building
        land_map={land:[float('inf')]*len(buildings) for land in lands}

        # BFS algo to find distance between each land and building
        def BFS(building_position):
            rowb,colb=buildings[building_position]
            q=deque()
            # Distance of building to self is 0
            q.append((rowb,colb,0))
            while q:
                row,col,dist=q.popleft()
                # We look in surrounding coordinates to find land
                # and if we find land we update distance of this building from land
                for i,j in [(row+1,col),(row-1,col),(row,col+1),(row,col-1)]:
                    # Any position which is 1 unit away dist is dist+1 inside this loop
                    #                     This clause checks whether distance of a piece of
                    #  land to that building is minimum or not. Once populated it'll'
                    # only change if another dist+1 is less than the current distance
                    if (i,j) in lands and land_map[(i,j)][building_position]>dist+1:
                        land_map[(i,j)][building_position]=dist+1
                        q.append((i,i,dist+1))

        for i in range(len(buildings)):
            BFS(i)
        # Find total sum of each building to land.Return min dist.
        min_dist=float('inf')
        for land in land_map:
            dist=sum(land_map[land])
            min_dist=min(min_dist,dist)
        return min_dist if min_dist!=float('inf') else -1










s=Solution()
# grid=[[1,0,2,0,1],[0,0,0,0,0],[0,0,1,0,0]]
# print(s.shortestDistance_naive_backtracking_recursion(grid))
# grid1=[[1,1],[0,1]]
# print(s.shortestDistance_naive_backtracking_recursion(grid1))
grid2=[[1,1,1,1,1,0],[0,0,0,0,0,1],[0,1,1,0,0,1],[1,0,0,1,0,1],[1,0,1,0,0,1],[1,0,0,0,0,1],[0,1,1,1,1,0]]
print(s.shortestDistance_my(grid2))


