# 56. Merge Intervals
#
# Given a collection of intervals, merge all overlapping intervals.
#
# Example 1:
#
# Input: intervals = [[1,3],[2,6],[8,10],[15,18]]
# Output: [[1,6],[8,10],[15,18]]
# Explanation: Since intervals [1,3] and [2,6] overlaps, merge them into [1,6].
# Example 2:
#
# Input: intervals = [[1,4],[4,5]]
# Output: [[1,5]]
# Explanation: Intervals [1,4] and [4,5] are considered overlapping.
# NOTE: input types have been changed on April 15, 2019. Please reset to default code definition to get new method signature.
#
# Constraints:
#
# intervals[i][0] <= intervals[i][1]


# Check this out another variation for facebook
# https://leetcode.com/problems/merge-intervals/solution/
class Solution(object):
    def sort_func(self,list):
        return list[0]

    def merge(self, intervals):
        size=len(intervals)

        list1=[]
        sorted_intervals=sorted(intervals,key=self.sort_func)
        merged=[sorted_intervals[0]]
        for index,elem in enumerate(sorted_intervals):
            if index+1<size:
                merged=self.merge_two_lists(merged[0],sorted_intervals[index+1])
            else:
                continue
            if len(merged)==2:
                list1.extend([merged[0]])
                merged=[merged[1]]
        list1.extend(merged)
        return list1


    def merge_two_lists(self,l1,l2):
        if l1[1]>=l2[0]:
            return [[min(l1[0],l2[0]),max(l2[1],l1[1])]]
        else:
            return [l1,l2]





s=Solution()
print(s.merge([[1,9],[2,5],[19,20],[10,11],[12,20],[2,3],[0,1],[1,2]]))
print(s.merge([[1,3],[2,6],[8,10],[15,18]]))
