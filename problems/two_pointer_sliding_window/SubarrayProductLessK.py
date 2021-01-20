# 713. Subarray Product Less Than K
#
# Your are given an array of positive integers nums.
#
# Count and print the number of (contiguous) subarrays where the product of all the elements in the subarray is less than k.
#
# Example 1:
# Input: nums = [10, 5, 2, 6], k = 100
# Output: 8
# Explanation: The 8 subarrays that have product less than 100 are: [10], [5], [2], [6], [10, 5], [5, 2], [2, 6], [5, 2, 6].
# Note that [10, 5, 2] is not included as the product of 100 is not strictly less than k.
# Note:
#
# 0 < nums.length <= 50000.
# 0 < nums[i] < 1000.
# 0 <= k < 10^6.
class Solution(object):
    # This is brute force intuitive not accepted by leetcode
    def numSubarrayProductLessThanK_naive(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: int
        """
        size=len(nums)
        left=0
        counter=0
        while left<size:
            right=left+1
            product=nums[left]
            if product<k:
                counter+=1
            while right<size:
                product=product*nums[right]
                if product<k:
                    counter+=1
                else:
                    break
                right+=1
            left+=1
        return counter



    # Only this is accepted in Leetcode
    # This is done by sliding window as all numbers are positive,
    # if there were negative numbers this wouldn't have been possible'
    def numSubarrayProductLessThanK_sliding(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: int
        """
        if k <= 1: return 0
        size=len(nums)
        counter=0
        left=0
        right=0
        product=1
        while right<size:
            product*=nums[right]
            while product>=k:
                product=product/nums[left]
                left+=1
            counter+=right-left +1
            right+=1
        return counter






s=Solution()
print(s.numSubarrayProductLessThanK_sliding([1,1,1],2))
print(s.numSubarrayProductLessThanK_sliding([1,-1,0],0))
print(s.numSubarrayProductLessThanK_sliding([28,54,7,-70,22,65,-6],100))



