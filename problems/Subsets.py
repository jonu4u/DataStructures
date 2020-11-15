# 78. Subsets
# Given an integer array nums, return all possible subsets (the power set).
#
# The solution set must not contain duplicate subsets.
# Example 1:
#
# Input: nums = [1,2,3]
# Output: [[],[1],[2],[1,2],[3],[1,3],[2,3],[1,2,3]]
# Example 2:
#
# Input: nums = [0]
# Output: [[],[0]]
#
#
# Constraints:
#
# 1 <= nums.length <= 10
# -10 <= nums[i] <= 10
class Solution(object):
    def subsets(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        out=[]
        size=len(nums)
        left=0
        while left<size:
            right=left+1
            out.append([nums[left]])
            while right<size:
                out.append([nums[left],nums[right]])
                right+=1
            left+=1
        out.append([])
        out.append(nums)
        return out