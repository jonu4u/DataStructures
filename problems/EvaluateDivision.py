# 399. Evaluate Division
#
# You are given an array of variable pairs equations and an array of real numbers values, where equations[i] = [Ai, Bi] and values[i] represent the equation Ai / Bi = values[i]. Each Ai or Bi is a string that represents a single variable.
#
# You are also given some queries, where queries[j] = [Cj, Dj] represents the jth query where you must find the answer for Cj / Dj = ?.
#
# Return the answers to all queries. If a single answer cannot be determined, return -1.0.
#
# Note: The input is always valid. You may assume that evaluating the queries will not result in division by zero and that there is no contradiction.
#
#
# Example 1:
#
# Input: equations = [["a","b"],["b","c"]], values = [2.0,3.0], queries = [["a","c"],["b","a"],["a","e"],["a","a"],["x","x"]]
# Output: [6.00000,0.50000,-1.00000,1.00000,-1.00000]
# Explanation:
# Given: a / b = 2.0, b / c = 3.0
# queries are: a / c = ?, b / a = ?, a / e = ?, a / a = ?, x / x = ?
# return: [6.0, 0.5, -1.0, 1.0, -1.0 ]
# Example 2:
#
# Input: equations = [["a","b"],["b","c"],["bc","cd"]], values = [1.5,2.5,5.0], queries = [["a","c"],["c","b"],["bc","cd"],["cd","bc"]]
# Output: [3.75000,0.40000,5.00000,0.20000]
# Example 3:
#
# Input: equations = [["a","b"]], values = [0.5], queries = [["a","b"],["b","a"],["a","c"],["x","y"]]
# Output: [0.50000,2.00000,-1.00000,-1.00000]
#
#
# Constraints:
#
# 1 <= equations.length <= 20
# equations[i].length == 2
# 1 <= Ai.length, Bi.length <= 5
# values.length == equations.length
# 0.0 < values[i] <= 20.0
# 1 <= queries.length <= 20
# queries[i].length == 2
# 1 <= Cj.length, Dj.length <= 5
# Ai, Bi, Cj, Dj consist of lower case English letters and digits.
from collections import defaultdict
class Solution(object):
    def calcEquation(self, equations, values, queries):
        """
        :type equations: List[List[str]]
        :type values: List[float]
        :type queries: List[List[str]]
        :rtype: List[float]
        """
        # We create the adjacency list from the nodes
        # which are elements in each equation
        sz=len(values)
        graph=defaultdict(list)
        for i in range(sz):
            equation=equations[i]
            value=values[i]
            u=equation[0]
            v=equation[1]
            graph[u].append((v,value))
            graph[v].append((u,1/value))

        out=[]
        for query in queries:
            out.append(self.get_path_value(query[0],query[1],graph))
        return out

    def get_path_value(self,v1,v2,graph):
        # We need to go from V1 to V2
        if v1 not in graph or v2 not in graph:
            return -1.0
        ans=float('inf')
        def bfs(v1,v2,is_visited,dist,ans):
            if v1==v2:
                ans=min(ans,dist)
                return ans
            if v1 in is_visited:
                return ans
            is_visited.add(v1)
            for node in graph[v1]:
                ans=bfs(node[0],v2,is_visited,dist*node[1],ans)
            is_visited.remove(v1)
            return ans
        ans=bfs(v1,v2,set(),1.0,ans)
        return -1.0 if ans==float('inf') else ans

    # Try this out using UNION FIND


s=Solution()
print(s.calcEquation([["a","b"],["b","c"]],
               [2.0,3.0],
               [["a","c"],["b","a"],["a","e"],["a","a"],["x","x"]]))

print(s.calcEquation([["x1","x2"],["x2","x3"],["x3","x4"],["x4","x5"]],
[3.0,4.0,5.0,6.0],
[["x1","x5"],["x5","x2"],["x2","x4"],["x2","x2"],["x2","x9"],["x9","x9"]]))

print(s.calcEquation([["a","b"],["c","d"]],
[1.0,1.0],
[["a","c"],["b","d"],["b","a"],["d","c"]]))