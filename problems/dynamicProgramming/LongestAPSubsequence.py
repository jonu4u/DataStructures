# 1218. Longest Arithmetic Subsequence of Given Difference
#
# Given an integer array arr and an integer difference, return the length of the longest subsequence in arr which is an arithmetic sequence such that the difference between adjacent elements in the subsequence equals difference.
#
#
#
# Example 1:
#
# Input: arr = [1,2,3,4], difference = 1
# Output: 4
# Explanation: The longest arithmetic subsequence is [1,2,3,4].
# Example 2:
#
# Input: arr = [1,3,5,7], difference = 1
# Output: 1
# Explanation: The longest arithmetic subsequence is any single element.
# Example 3:
#
# Input: arr = [1,5,7,8,5,3,4,2,1], difference = -2
# Output: 4
# Explanation: The longest arithmetic subsequence is [7,5,3,1].
#
#
# Constraints:
#
# 1 <= arr.length <= 10^5
# -10^4 <= arr[i], difference <= 10^4
class Solution(object):
    def __init__(self):
        # self.memo=[[1 for i in range(0,10000+1)]for i in range(0,10000+1)]
        self.max_len=1

   # This is failing when we have same length multiple subsequences
    def longestSubsequence_dp_top_down(self, arr, difference,start_index,next_index):
        """
        :type arr: List[int]
        :type difference: int
        :rtype: int
        """
        if start_index==len(arr)-1 or next_index==len(arr):
            return 1
        if start_index>len(arr)-1 or next_index>len(arr):
            return 0

        if arr[next_index]-arr[start_index]==difference:
            length= 1+ self.longestSubsequence_dp_top_down(arr,difference,next_index,next_index+1)
            self.max_len=max(self.max_len,length)
            return self.max_len
        left=self.longestSubsequence_dp_top_down(arr,difference,start_index,next_index+1)
        right=self.longestSubsequence_dp_top_down(arr,difference,start_index+1,start_index+2)
        self.max_len=max(self.max_len,left,right)
        return self.max_len

    # This causes TLE in Leetcode
    def longestSubsequence_naive(self, arr, difference):
        """
        :type arr: List[int]
        :type difference: int
        :rtype: int
        """
        size=len(arr)
        if size<3:
            return size
        longest=1
        count=1
        left=0
        begin=0
        while begin<size-1:
            right=left+1
            while right<size:
                if arr[right]-arr[left]==difference:
                    count+=1
                    left=right
                right+=1
            longest=max(longest,count)
            if longest==size:
                return longest
            count=1
            begin+=1
            left=begin
        return longest

s=Solution()
print(s.longestSubsequence_naive([1,2,3,4],1))
print(s.longestSubsequence_naive([1,5,7,8,5,3,4,2,1],-2))
print(s.longestSubsequence_naive([3,0,-3,4,-4,7,6],3))
print(s.longestSubsequence_naive([6,-2,0,3,-7,6,-5,-8],-5))
print("Below -----------")
# s.longestSubsequence_dp_top_down([1,2,3,4],1,0,1)
# print(s.max_len)
s.longestSubsequence_dp_top_down([1,5,7,8,5,3,4,2,1],-2,0,1)
print(s.max_len)
# s.longestSubsequence_dp_top_down([3,0,-3,4,-4,7,6],3,0,1)
# print(s.max_len)
# s.longestSubsequence_dp_top_down([6,-2,0,3,-7,6,-5,-8],-5,0,1)
# print(s.max_len)


