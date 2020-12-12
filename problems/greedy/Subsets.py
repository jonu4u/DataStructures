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
    # We take cascading approach. This means we add one char
    # from nums and do all possible combinations of the elements
    # in return map
    def subsets_single_line(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        out=[[]]
        for elem in nums:
            out+=[curr +[elem] for curr in out]
        return out

    def subsets(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        out=[]
        for elem in nums:
            list1=[]
            for i in out:
                list1.append(i+[elem])
            out.extend(list1[:])
            out.append([elem])
        out.append([])
        return out

s=Solution()
print(s.subsets_single_line([1,2,3]))
print(s.subsets([1,2,3]))

