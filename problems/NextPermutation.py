# Implement next permutation, which rearranges numbers into the lexicographically next greater permutation of numbers.
#
# If such an arrangement is not possible, it must rearrange it as the lowest possible order (i.e., sorted in ascending order).
#
# The replacement must be in place and use only constant extra memory.
#
#
#
# Example 1:
#
# Input: nums = [1,2,3]
# Output: [1,3,2]
# Example 2:
#
# Input: nums = [3,2,1]
# Output: [1,2,3]
# Example 3:
#
# Input: nums = [1,1,5]
# Output: [1,5,1]
# Example 4:
#
# Input: nums = [1]
# Output: [1]

class Solution(object):
    # This solution is correct but leetcode wants in place list modification without taking new list
    def nextPermutation(self, nums):
        original=nums[:]
        size=len(nums)
        if size<2:
            return nums
        right=size-1
        while(right>0):
            if nums[right]>nums[right-1]:
                break
            right-=1
        decision_index=right-1
        rev=nums[right:]
        rev.reverse()
        nums=nums[:right]+rev
        for index,elem in enumerate(nums):
            if index>decision_index:
                if nums[decision_index]<elem:
                    nums[decision_index],nums[index]=nums[index],nums[decision_index]
                    break
        if nums==original:
            sorted(nums)
        return nums

    # IN THIS SOLUTION NO NEW LIST CAN BE TAKEN
    def nextPermutation_in_same_list(self, nums):
        original=nums[:]
        size=len(nums)
        if size<2:
            return nums
        right=size-1
        while(right>0):
            if nums[right]>nums[right-1]:
                break
            right-=1
        decision_index=right-1
        self.reverse(nums,right)
        for index,elem in enumerate(nums):
            if index>decision_index:
                if nums[decision_index]<elem:
                    nums[decision_index],nums[index]=nums[index],nums[decision_index]
                    break
        if nums==original:
            sorted(nums)

    def reverse(self,nums,index):
        left=index
        right=len(nums)-1
        while left<right:
            nums[left],nums[right]=nums[right],nums[left]
            left+=1
            right-=1





s=Solution()
print(s.nextPermutation([1,2,3]))
print(s.nextPermutation([3,2,1]))
print(s.nextPermutation([1,1,5]))

print("------")
print(s.nextPermutation_in_same_list([1,2,3]))
print(s.nextPermutation_in_same_list([3,2,1]))
print(s.nextPermutation_in_same_list([1,1,5]))