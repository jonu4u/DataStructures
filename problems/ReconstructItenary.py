# 332. Reconstruct Itinerary
#
# Given a list of airline tickets represented by pairs of departure and arrival airports [from, to], reconstruct the itinerary in order. All of the tickets belong to a man who departs from JFK. Thus, the itinerary must begin with JFK.
#
# Note:
#
# If there are multiple valid itineraries, you should return the itinerary that has the smallest lexical order when read as a single string. For example, the itinerary ["JFK", "LGA"] has a smaller lexical order than ["JFK", "LGB"].
# All airports are represented by three capital letters (IATA code).
# You may assume all tickets form at least one valid itinerary.
# One must use all the tickets once and only once.
# Example 1:
#
# Input: [["MUC", "LHR"], ["JFK", "MUC"], ["SFO", "SJC"], ["LHR", "SFO"]]
# Output: ["JFK", "MUC", "LHR", "SFO", "SJC"]
# Example 2:
#
# Input: [["JFK","SFO"],["JFK","ATL"],["SFO","ATL"],["ATL","JFK"],["ATL","SFO"]]
# Output: ["JFK","ATL","JFK","SFO","ATL","SFO"]
# Explanation: Another possible reconstruction is ["JFK","SFO","ATL","JFK","ATL","SFO"].
# But it is larger in lexical order.

from collections import defaultdict
from collections import deque
class Solution(object):
    def findItinerary(self, tickets):
        """
        :type tickets: List[List[str]]
        :rtype: List[str]
        """
        graph=defaultdict(list)
        # Taking begin point into consideration
        journey=len(tickets)+1
        for ticket in tickets:
            departure=ticket[0]
            arrival=ticket[1]
            graph[departure].append(arrival)
        # So we have our directed graph and adjacency list

        stack=deque()
        out=[]
        stack.appendleft("JFK")
        while stack:
            # We check the top element of stack
            curr_node=stack.popleft()
            # if the top elem is a key with values
            if graph.get(curr_node):
                # we append the 1st element of the values(sorted)
                # in begining of stack,remove that element from graph
                stack.appendleft(curr_node)
                # We need to sort because we want the ans in lexicographic order
                adj_list=sorted(graph[curr_node])
                stack.appendleft(adj_list[0])
                adj_list.pop(0)
                graph[curr_node]=adj_list
            # If key not found we pop and append in return list
            else:
                out.append(curr_node)
        # We reverse and return the final list
        out.reverse()
        return out

s=Solution()
print(s.findItinerary([["MUC", "LHR"], ["JFK", "MUC"], ["SFO", "SJC"], ["LHR", "SFO"]]))
print(s.findItinerary([["JFK","SFO"],["JFK","ATL"],["SFO","ATL"],["ATL","JFK"],["ATL","SFO"]]))
print(s.findItinerary([["JFK","KUL"],["JFK","NRT"],["NRT","JFK"]]))
print(s.findItinerary([["JFK","AAA"],["AAA","JFK"],["JFK","BBB"],["JFK","CCC"],["CCC","JFK"]]))








