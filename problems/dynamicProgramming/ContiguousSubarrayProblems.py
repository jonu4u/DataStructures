# Largest Sum Contiguous Subarray
# # Write an efficient program to find the sum of contiguous subarray within a one-dimensional array of numbers which has the largest sum.
# # kadane-algorithm
# https://www.geeksforgeeks.org/largest-sum-contiguous-subarray/
class Kadane:
    # Algo
# Initialize:
# max_so_far = 0
# max_ending_here = 0
#
# Loop for each element of the array
# (a) max_ending_here = max_ending_here + a[i]
# (b) if(max_so_far < max_ending_here)
# max_so_far = max_ending_here
# (c) if(max_ending_here < 0)
# max_ending_here = 0
# return max_so_far
    def contiguous_max_sum(self,arr):
         max_so_far=float('-inf')
         max_ending_here=0
         for elem in arr:
             max_ending_here+=elem
             if max_ending_here<elem:
                 max_ending_here=elem
             if max_so_far<max_ending_here:
                 max_so_far=max_ending_here
         return max_so_far

    #     152. Maximum Product Subarray
    # Given an integer array nums, find the contiguous subarray within an array (containing at least one number) which has the largest product.
    #
    # Example 1:
    #
    # Input: [2,3,-2,4]
    # Output: 6
    # Explanation: [2,3] has the largest product 6.
    # Example 2:
    #
    # Input: [-2,0,-1]
    # Output: 0
    # Explanation: The result cannot be 2, because [-2,-1] is not a subarray.

#     Approach 2: Dynamic Programming
# Intuition
#
# Rather than looking for every possible subarray to get the largest product, we can scan the array and solve smaller subproblems.
#
# Let's see this problem as a problem of getting the highest combo chain. The way combo chains work is that they build on top of the previous combo chains that you have acquired. The simplest case is when the numbers in nums are all positive numbers. In that case, you would only need to keep on multiplying the accumulated result to get a bigger and bigger combo chain as you progress.
#
# However, two things can disrupt your combo chain:
#
# Zeros
# Negative numbers
# Zeros will reset your combo chain. A high score which you have achieved will be recorded in placeholder result. You will have to restart your combo chain after zero. If you encounter another combo chain which is higher than the recorded high score in result, you just need to update the result.
#
# Negative numbers are a little bit tricky. A single negative number can flip the largest combo chain to a very small number. This may sound like your combo chain has been completely disrupted but if you encounter another negative number, your combo chain can be saved. Unlike zero, you still have a hope of saving your combo chain as long as you have another negative number in nums (Think of this second negative number as an antidote for the poison that you just consumed). However, if you encounter a zero while you are looking your another negative number to save your combo chain, you lose the hope of saving that combo chain.
#
# While going through numbers in nums, we will have to keep track of the maximum product up to that number (we will call max_so_far) and minimum product up to that number (we will call min_so_far). The reason behind keeping track of max_so_far is to keep track of the accumulated product of positive numbers. The reason behind keeping track of min_so_far is to properly handle negative numbers.
#
# max_so_far is updated by taking the maximum value among:
#
# Current number.
# This value will be picked if the accumulated product has been really bad (even compared to the current number). This can happen when the current number has a preceding zero (e.g. [0,4]) or is preceded by a single negative number (e.g. [-3,5]).
# Product of last max_so_far and current number.
# This value will be picked if the accumulated product has been steadily increasing (all positive numbers).
# Product of last min_so_far and current number.
# This value will be picked if the current number is a negative number and the combo chain has been disrupted by a single negative number before (In a sense, this value is like an antidote to an already poisoned combo chain).
# min_so_far is updated in using the same three numbers except that we are taking minimum among the above three numbers.
#
# In the animation below, you will observe a negative number -5 disrupting a combo chain but that combo chain is later saved by another negative number -4. The only reason this can be saved is because of min_so_far. You will also observe a zero disrupting a combo chain.
    def maxProduct(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        if len(nums)==1:
            return nums[0]
        max_so_far=min_so_far=nums[0]
        result=max_so_far
        for i in range(1,len(nums)):
            temp_max=max(nums[i],max_so_far*nums[i],min_so_far*nums[i])
            min_so_far=min(nums[i],max_so_far*nums[i],min_so_far*nums[i])
            max_so_far=temp_max
            result=max(result,max_so_far)
        return result


# 209. Minimum Size Subarray Sum
#
# Given an array of n positive integers and a positive integer s, find the minimal length of a contiguous subarray of which the sum ≥ s. If there isn't one, return 0 instead.
#
# Example:
#
# Input: s = 7, nums = [2,3,1,2,4,3]
# Output: 2
# Explanation: the subarray [4,3] has the minimal length under the problem constraint.

# The mdium level has less test cases but the hard one is difficult with lot of test cases
#     https://leetcode.com/problems/shortest-subarray-with-sum-at-least-k/submissions/
    def minSubArrayLen(self, s, nums):
        """
        :type s: int
        :type nums: List[int]
        :rtype: int
        """
        size=len(nums)
        # If length is 0 return 0 no match
        if size==0:
            return 0

        left=0
        right=left+1
        prev_right=0
        sum=nums[left]
        ctr=1
        max_ctr=float('inf')
        # If the 1st element acheive >= target then return 1
        if sum>=s:
            return 1
        # This sliding window in one pass
        while left<size-1:
            # we take 3 pointers left and right and prev right,
            # whenever in a window we reach >=s we
            # remove from left, till we're less than s and we then add right
            # We increase and decrease counter when we add and remove element
            if right<size and prev_right!=right:
                sum=sum+nums[right]
                # The prev pointer needs to check whether we're increasing right or not
                # and we keep on decreasing from left.
                prev_right=right
                ctr+=1
            if sum>=s:
                max_ctr=min(max_ctr,ctr)
                ctr-=1
                sum=sum-nums[left]
                left+=1
            elif right<size:
                right+=1
            elif right>=size:
                sum=sum-nums[left]
                left+=1
                ctr-=1
        # If there is no match return 0
        return max_ctr if max_ctr!=float('inf') else 0

s=Kadane()
print(s.minSubArrayLen(4,[2,3,1,2,4,3]))
print(s.minSubArrayLen(167,[84,-37,32,40,95]))
print(s.minSubArrayLen(89,[-28,81,-20,28,-29]))