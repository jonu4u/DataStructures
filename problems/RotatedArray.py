# 33. Search in Rotated Sorted Array
#
# You are given an integer array nums sorted in ascending order, and an integer target.
#
# Suppose that nums is rotated at some pivot unknown to you beforehand (i.e., [0,1,2,4,5,6,7] might become [4,5,6,7,0,1,2]).
#
# If target is found in the array return its index, otherwise, return -1.
#
#
#
# Example 1:
#
# Input: nums = [4,5,6,7,0,1,2], target = 0
# Output: 4
# Example 2:
#
# Input: nums = [4,5,6,7,0,1,2], target = 3
# Output: -1
# Example 3:
#
# Input: nums = [1], target = 0
# Output: -1
#
#
# Constraints:
#
# 1 <= nums.length <= 5000
# -10^4 <= nums[i] <= 10^4
# All values of nums are unique.
# nums is guranteed to be rotated at some pivot.
# -10^4 <= target <= 10^4


class Solution(object):
    def search(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        size=len(nums)
        # Till array of len 3 we can find quickly by iterative
        if size<4:
            if target in nums:
                return nums.index(target)
            return -1
        # Find the pivot_index
        pivot_index=self.find_pivot_index(nums,nums)
        # If pivot is inf that means there is no pivot simply bin search to find index of target
        if pivot_index==float('-inf'):
            return self.find_number(nums,nums,target)
        elif target==nums[pivot_index]:
            return pivot_index
        end_elem=nums[len(nums)-1]
        # if the target is more than the last element the target must be within start to pivot index
        if target>end_elem:
            return self.find_number(nums[:pivot_index],nums,target)
        # Else number is from pivot to end
        elif target>nums[pivot_index]:
            return self.find_number(nums[pivot_index:],nums,target)
        # If not found return -1
        return -1


    # This is a recursive function getting the pivot index
    def find_pivot_index(self,nums,original_nums):
        size=len(nums)
        mid=size//2
        start=nums[0]
        end=nums[size-1]
        # if the start and end is same that means the current element is the pivot
        if start==end:
            return original_nums.index(start)
        # if the start<mid element <end and length is original that means the array is not pivoted so return inf
        if start<nums[mid] and nums[mid]<end and size==len(original_nums):
            return float('-inf')
        # if the pivot lies -1 or +1 from mid
        elif mid+1<size and nums[mid]>nums[mid+1]:
            return original_nums.index(nums[mid+1])
        elif mid-1>-1 and nums[mid-1]>nums[mid]:
            return original_nums.index(nums[mid])
        # The array after mid index
        rest_num=nums[mid+1:]
        start=rest_num[0]
        end=rest_num[len(rest_num)-1]
        # if this rest array is size 1 or the start<mid of this rest array=<end that means
        #     the pivot lies in the part of start to mid range
        if start==end or (start<rest_num[len(rest_num)//2] and rest_num[len(rest_num)//2]<=end):
            return self.find_pivot_index(nums[:mid+1],original_nums)
        # Pivot is in the rest of the array
        else:
            return self.find_pivot_index(rest_num,original_nums)

    def find_number(self,nums,original_nums,number):
        size=len(nums)
        mid=size//2
        while True:
            # if the size is 1 then we just check for the number
            if len(nums)==1:
                if nums[0]==number:
                    return original_nums.index(nums[0])
                return -1
            # This is binary search logic
            if number<nums[mid]:
                nums=nums[:mid]
                mid=len(nums)//2
            elif number==nums[mid]:
                return original_nums.index(nums[mid])
            else:
                nums=nums[mid:]
                mid=len(nums)//2



s=Solution()
print(s.find_pivot_index([4,5,6,7,8,9],[4,5,6,7,8,9]))
print(s.find_pivot_index([4,5,6,7,0,1,2],[4,5,6,7,0,1,2]))
print(s.find_pivot_index([9,10,11,13,14,15,3],[9,10,11,13,14,15,3]))
print(s.find_pivot_index([9,10,11,12,13,2,3],[9,10,11,12,13,2,3]))
print(s.find_pivot_index([7,8,1,2,3,4,5,6],[7,8,1,2,3,4,5,6]))
print(s.find_pivot_index([4,5,6,7,0,1,2],[4,5,6,7,0,1,2]))
print(s.find_pivot_index([4,5,6,7,8,9,1,2,3],[4,5,6,7,8,9,1,2,3]))
print(s.find_pivot_index([5,1,2,3,4],[5,1,2,3,4]))
print(s.find_pivot_index([9,1,2,3,4],[9,1,2,3,4]))
#
print(s.find_number([0,1,2],[4,5,6,7,0,1,2],1))


