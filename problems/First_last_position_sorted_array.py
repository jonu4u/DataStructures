# 34. Find First and Last Position of Element in Sorted Array

# Given an array of integers nums sorted in ascending order, find the starting and ending position of a given target value.
#
# If target is not found in the array, return [-1, -1].
#
# Follow up: Could you write an algorithm with O(log n) runtime complexity?
#
#
#
# Example 1:
#
# Input: nums = [5,7,7,8,8,10], target = 8
# Output: [3,4]
# Example 2:
#
# Input: nums = [5,7,7,8,8,10], target = 6
# Output: [-1,-1]
# Example 3:
#
# Input: nums = [], target = 0
# Output: [-1,-1]
#
#
# Constraints:
#
# 0 <= nums.length <= 105
# -109 <= nums[i] <= 109
# nums is a non-decreasing array.
# -109 <= target <= 109

class Solution(object):
    def searchRange(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        default=[-1,-1]
        size=len(nums)
        if size==0:
            return default
        staring_index=self.find_target_index(nums,target,nums)
        if staring_index==-1:
            return default
        else:
            default[0]=staring_index
            while staring_index<size and nums[staring_index]==target:
                staring_index+=1
            default[1]=staring_index-1
            return default

    # TODO Try to find the last occurence of the digit
    # def find_target_index(self,nums,target,orig_num):
    #     size=len(nums)
    #     mid=size//2
    #
    #     if mid==0:
    #         if target==nums[0]:
    #             return orig_num.index(target)
    #         return -1
    #     if nums[mid]==target:
    #         return orig_num.index(target)
    #     if nums[mid]>=target:
    #         return self.find_target_index(nums[:mid],target,orig_num)
    #     else:
    #         return self.find_target_index(nums[mid:],target,orig_num)

    def find_target_index(self,nums,target,orig_num):
        size=len(nums)
        mid=size//2

        if mid==0:
            if target==nums[0]:
                return orig_num.index(target)
            return -1
        if nums[mid]==target:
            return orig_num.index(target)
        if nums[mid]>target:
            return self.find_target_index(nums[:mid],target,orig_num)
        else:
            return self.find_target_index(nums[mid:],target,orig_num)



s=Solution()
print(s.find_target_index([4,5,13,20,21,21,21,21,22],21,[4,5,13,20,21,21,21,21,22]))
print(s.find_target_index([4,5,13,20,21,21,21,21,22],4,[4,5,13,20,21,21,21,21,22]))
print(s.find_target_index([4,5,13,20,21,21,21,21,22],22,[4,5,13,20,21,21,21,21,22]))
print(s.find_target_index([4,5,13,13,20,21,21,21,21,22],13,[4,5,13,13,20,21,21,21,21,22]))
print(s.find_target_index([4,5,13,20,21,21,21,21,22],20,[4,5,13,20,21,21,21,21,22]))
print(s.find_target_index([4],5,[4]))
print(s.searchRange([5,7,7,8,8,10],8))
print(s.searchRange([4,5,13,20,21,21,21,21,22],21))
print(s.searchRange([4],4))
