# 994. Rotting Oranges
#
# In a given grid, each cell can have one of three values:
#
# the value 0 representing an empty cell;
# the value 1 representing a fresh orange;
# the value 2 representing a rotten orange.
# Every minute, any fresh orange that is adjacent (4-directionally) to a rotten orange becomes rotten.
#
# Return the minimum number of minutes that must elapse until no cell has a fresh orange.  If this is impossible, return -1 instead.
#
#
#
# Example 1:
#
#
#
# Input: [[2,1,1],[1,1,0],[0,1,1]]
# Output: 4
# Example 2:
#
# Input: [[2,1,1],[0,1,1],[1,0,1]]
# Output: -1
# Explanation:  The orange in the bottom left corner (row 2, column 0) is never rotten, because rotting only happens 4-directionally.
# Example 3:
#
# Input: [[0,2]]
# Output: 0
# Explanation:  Since there are already no fresh oranges at minute 0, the answer is just 0.
#
#
# Note:
#
# 1 <= grid.length <= 10
# 1 <= grid[0].length <= 10
# grid[i][j] is only 0, 1, or 2.
# Accepted
# 179,122
# Submissions
# 362,166
from collections import deque
class Solution(object):
    def orangesRotting(self, grid):
        """
        :type grid: List[List[int]]
        :rtype: int
        """
        # We find the number of fresh oranges
        # and put the positions of rotten oranges in a queue
        numberOfFreshOranges=0
        rotten_orange_q=deque()
        row_len=len(grid)
        col_len=len(grid[0])
        for row in range(row_len):
            for col in range(col_len):
                if grid[row][col]==1:
                    numberOfFreshOranges+=1
                elif grid[row][col]==2:
                    rotten_orange_q.append((row,col))
        if numberOfFreshOranges==0:
            return 0

        # We mark the end of he rotten numberOfFreshOrangeswith None
        # so that it means every minute till we get None,
        # we'll mark all adjacent fresh oranges
        rotten_orange_q.append(None)
        minute=0
        # We keep a count of rotten
        rotten_count=0
        while rotten_orange_q:
            curr_rotten=rotten_orange_q.popleft()
            # If the last None is popped that means
            # there is no more orage to rot, we break
            if not curr_rotten and len(rotten_orange_q)==0 :
                break
            # If there are more oranges in q we
            # add 1 minute and we say this level is
            # finished and we mark the end of next level
            # as None
            elif not curr_rotten:
                minute+=1
                rotten_orange_q.append(None)
                continue
            x,y=curr_rotten

            # We check for adjacent fresh oranges f found we rot it and append that
            #     rotten orange to the q which will be checked in next minute for
            #     its adjacent fresh oranges
            for i,j in [(x+1,y),(x-1,y),(x,y+1),(x,y-1)]:
                if i<0 or j<0 or i>=row_len or j>=col_len or grid[i][j]!=1:
                    continue
                grid[i][j]=2
                rotten_orange_q.append((i,j))
                # Every time we found a fresh orange and make it rotten
                # we increase the rotten count
                rotten_count+=1
            if rotten_count==numberOfFreshOranges:
                # If we have exhausted all fresh ornages
                # we exit and add up the minute
                minute+=1
                break
        # We can come here if there is some boundary between
        # fresh and rotten and all oranges can't be rotten
        if rotten_count<numberOfFreshOranges or minute==0:
            return -1
        return minute