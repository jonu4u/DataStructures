# 210. Course Schedule II
#
# There are a total of n courses you have to take labelled from 0 to n - 1.
#
# Some courses may have prerequisites, for example, if prerequisites[i] = [ai, bi] this means you must take the course bi before the course ai.
#
# Given the total number of courses numCourses and a list of the prerequisite pairs, return the ordering of courses you should take to finish all courses.
#
# If there are many valid answers, return any of them. If it is impossible to finish all courses, return an empty array.
# Example 1:
#
# Input: numCourses = 2, prerequisites = [[1,0]]
# Output: [0,1]
# Explanation: There are a total of 2 courses to take. To take course 1 you should have finished course 0. So the correct course order is [0,1].
# Example 2:
#
# Input: numCourses = 4, prerequisites = [[1,0],[2,0],[3,1],[3,2]]
# Output: [0,2,1,3]
# Explanation: There are a total of 4 courses to take. To take course 3 you should have finished both courses 1 and 2. Both courses 1 and 2 should be taken after you finished course 0.
# So one correct course order is [0,1,2,3]. Another correct ordering is [0,2,1,3].
# Example 3:
#
# Input: numCourses = 1, prerequisites = []
# Output: [0]
#
#
# Constraints:
#
# 1 <= numCourses <= 2000
# 0 <= prerequisites.length <= numCourses * (numCourses - 1)
# prerequisites[i].length == 2
# 0 <= ai, bi < numCourses
# ai != bi
# All the pairs [ai, bi] are distinct.
from collections import deque
class Solution(object):
    def findOrder(self, numCourses, prerequisites):
        """
        :type numCourses: int
        :type prerequisites: List[List[int]]
        :rtype: List[int]
        """
        # This is Also topological sort
        # Each prereq is a relation where for doing prereq[0] we need to do prereq[1]
        graph={i:[] for i in range(numCourses)}
        indegree=[0]*numCourses

        # Populate graph with relations and indegree list
        for prereq in prerequisites:
            to_course=prereq[0]
            from_course=prereq[1]
            graph[from_course].append(to_course)
            indegree[to_course]+=1

        # Do BFS with q for topo sort
        q=deque()
        for index,elem in enumerate(indegree):
            if elem==0:
                q.append(index)
        out=[]
        while len(q)>0:
            current=q.popleft()
            out.append(current)
            adj_list=graph[current]
            for node in adj_list:
                indegree[node]-=1
                if indegree[node]==0:
                    q.append(node)
        return out if len(out)==len(graph) else []

# Same qstn is course sched 1 only there we have to return boolean
