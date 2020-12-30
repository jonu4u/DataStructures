# 560. Subarray Sum Equals K
# Given an array of integers nums and an integer k, return the total number of continuous subarrays whose sum equals to k.
#
#
#
# Example 1:
#
# Input: nums = [1,1,1], k = 2
# Output: 2
# Example 2:
#
# Input: nums = [1,2,3], k = 3
# Output: 2
#
#
# Constraints:
#
# 1 <= nums.length <= 2 * 104
# -1000 <= nums[i] <= 1000
# -107 <= k <= 107
class Solution(object):
    # This is brute force intuitive not accepted by leetcode
    def subarraySum_naive(self, nums, k):
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
            sum=nums[left]
            if sum==k:
                counter+=1
            while right<size:
                sum=sum+nums[right]
                if sum==k:
                    counter+=1
                right+=1
            left+=1
        return counter

    # Take cumulate sum and at each step remove the preceeding elements and check if
    # the sum equals target.This is also TLE in leetcode
    def subarraySum_cumulative(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: int
        """
        size=len(nums)
        index=1
        cumulative_array=[]
        cum_sum=nums[0]
        cumulative_array.append(cum_sum)
        while index<size:
            cum_sum=cum_sum+nums[index]
            cumulative_array.append(cum_sum)
            index+=1
        counter=0
        left,right=0,len(cumulative_array)-1
        while right>0:
            subarrsum=cumulative_array[right]
            if subarrsum==k:
                counter+=1
            while left<right:
                 subarrsum=cumulative_array[right]
                 subarrsum=subarrsum-cumulative_array[left]
                 if subarrsum==k:
                     counter+=1
                 left+=1
            left=0
            right-=1
        return counter

    # Only this is accepted in Leetcode
    # This is done using prefix sum technique
    # https://www.youtube.com/watch?v=XVAMnJluQIk&t=17
    # [-1,2,-1,0] sum(2)=0 sum(3)=0 so basically we can say sum of element from 2 to 3 is also 0
    def subarraySum_hashmap(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: int
        """
        size=len(nums)
        counter=0
        map={}
        # Initilize the map with sum 0 seen one time
        map[0]=1
        sum=0
        for i in range(0,size):
            # this sum is the cumulative sum
            sum=sum+nums[i]
            # so if the diff of this cumulative sum and k is present in the map,
            # it means that is also count of the sum present
            if (sum-k) in map:
                counter=counter+map.get(sum-k)
            # If diff is not present add the present sum in the map with count 1
            map[sum]=map.get(sum,0)+1
        return counter






s=Solution()
print(s.subarraySum_naive([1,1,1],2))
print(s.subarraySum_naive([1,-1,0],0))
print(s.subarraySum_naive([28,54,7,-70,22,65,-6],100))
print("-----------")
print(s.subarraySum_hashmap([1,1,1],2))
print(s.subarraySum_hashmap([1,-1,0],0))
print(s.subarraySum_hashmap([28,54,7,-70,22,65,-6],100))


