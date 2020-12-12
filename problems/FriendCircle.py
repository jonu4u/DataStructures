# 547. Friend Circles
#
# There are N students in a class. Some of them are friends, while some are not. Their friendship is transitive in nature. For example, if A is a direct friend of B, and B is a direct friend of C, then A is an indirect friend of C. And we defined a friend circle is a group of students who are direct or indirect friends.
#
# Given a N*N matrix M representing the friend relationship between students in the class. If M[i][j] = 1, then the ith and jth students are direct friends with each other, otherwise not. And you have to output the total number of friend circles among all the students.
#
# Example 1:
#
# Input:
# [[1,1,0],
#  [1,1,0],
#  [0,0,1]]
# Output: 2
# Explanation:The 0th and 1st students are direct friends, so they are in a friend circle.
# The 2nd student himself is in a friend circle. So return 2.
#
#
# Example 2:
#
# Input:
# [[1,1,0],
#  [1,1,1],
#  [0,1,1]]
# Output: 1
# Explanation:The 0th and 1st students are direct friends, the 1st and 2nd students are direct friends,
# so the 0th and 2nd students are indirect friends. All of them are in the same friend circle, so return 1.
#
#
#
# Constraints:
#
# 1 <= N <= 200
# M[i][i] == 1
# M[i][j] == M[j][i]
from collections import defaultdict
class Solution(object):
    def findCircleNum_naive(self, M):
        """
        :type M: List[List[int]]
        :rtype: int
        """
        # Simple DFS on graph with adjacency matrix will do
        row_len=len(M)
        col_len=len(M[0])
        graph=defaultdict(list)

        # here we create the adjacency list from matrix
        for row in range(row_len):
            for col in range(col_len):
                if row==col:
                    continue
                if M[row][col]==1:
                    graph[row].append(col)
        # The adjacency list is created
        # We can do dfs/bfs on this, let's do dfs
        is_visited=set()
        circle=0
        for key in graph.keys():
            if key in is_visited:
                continue
            circle+=1
            self.dfs(is_visited,key,graph)
            if len(is_visited)==len(graph):
                return (row_len-len(graph)) +circle

        return (row_len-len(graph)) +circle




    def dfs(self,is_visited,start,graph):
        # For each element we look in the
        # graph for this elemnt as key
        #     and if found we again look into each
        # element. Once an element is visisted we mark it is visitred
        if start in is_visited:
            return is_visited
        is_visited.add(start)
        for adj in graph[start]:
            self.dfs(is_visited,adj,graph)
        return is_visited


    # This solution we directly do dfs on the matrix
    def findCircleNum(self, M):
        """
        :type M: List[List[int]]
        :rtype: int
        """
        # Simple DFS on graph with adjacency matrix will do
        row_len=len(M)
        col_len=len(M[0])
        is_visited=set()
        circle=0
        # We look over each row and col in grid
        # wheneever row!=col and we have a 1 it means
        # that row element is related to that column element
        for row in range(row_len):
            # If we have visited all the nodes we return circle
            if len(is_visited)==row_len:
                return circle
            # If we have already visisted a row, skip that row
            if row in is_visited:
                continue
            for col in range(col_len):
                if row==col:
                    continue
                # Whenever we find a node, we do dfs
                if M[row][col]==1:
                    if col in is_visited:
                        continue
                    # We start dfs putting the element in col
                    # in the dfs method
                    is_visited=self.dfs_smart(is_visited,col,M)
            circle+=1
            is_visited.add(row)
        # If there is no connecting node, we found those out and add it to circle
        # as each such node is circle by itself as per problem
        return circle+(row_len-len(is_visited))



    def dfs_smart(self,is_visited,row,graph):
        # The column which is passed, that column is used as abs(row and we check all
        # elements of that row for each columns to find element except itself
        col_len=len(graph[0])
        for i in range(col_len):
            if row==i or i in is_visited:
                continue
            if graph[row][i]==1:
                # We add the connected node in is_visitedand pass this
                # node in recursion to find it's corresponding
                # connected nodes, dfs
                is_visited.add(i)
                self.dfs(is_visited,i,graph)
        # Once we visit all  connected nodes, we mark the parent row as visisted
        is_visited.add(row)
        return is_visited








