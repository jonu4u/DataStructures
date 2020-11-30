# 42. Trapping Rain Water
#
# Given n non-negative integers representing an elevation map where the width of each bar is 1, compute how much water it can trap after raining.
#
# Example 1:
#
#
# Input: height = [0,1,0,2,1,0,1,3,2,1,2,1]
# Output: 6
# Explanation: The above elevation map (black section) is represented by array [0,1,0,2,1,0,1,3,2,1,2,1]. In this case, 6 units of rain water (blue section) are being trapped.
# Example 2:
#
# Input: height = [4,2,0,3,2,5]
# Output: 9
# https://leetcode.com/problems/trapping-rain-water/solution/
class Solution(object):
    def trap(self, height):
        """
        :type height: List[int]
        :rtype: int
        """
        size=len(height)
        if size<2:
            return 0
        left_arr,right_arr=[0]*size,[0]*size
        # So iterate array from left to right from max of each element between it and previous
        left_arr[0]=height[0]
        for i in range(1,size):
            left_arr[i]=max(left_arr[i-1],height[i])
        # Iterate again from right to left to find maximum from right between current and right
        right_arr[size-1]=height[size-1]
        for i in range(size-2,-1,-1):
            right_arr[i]=max(right_arr[i+1],height[i])

        sum=0
        # For each element min of left and right - height is the sum
        for i in range(0,size):
            sum+=min(left_arr[i],right_arr[i])-height[i]
        return sum

    def trap_fast(self, height):
        """
        :type height: List[int]
        :rtype: int
        """
        size=len(height)
        if size<2:
            return 0
        left_arr,right_arr=[0]*size,[0]*size
        # So iterate array from left to right from max of each element between it and previous
        left_arr[0]=height[0]
        right_arr[size-1]=height[size-1]
        # Using two pointers to populate two arrays simulataneously
        # we populate the arrays in one pass and redce one loop
        for i in range(1,size):
            left=i
            right=size-1-i
            left_arr[left]=max(left_arr[left-1],height[left])
            right_arr[right]=max(right_arr[right+1],height[right])
        sum=0
        # For each element min of left and right - height is the sum
        for i in range(0,size):
            sum+=min(left_arr[i],right_arr[i])-height[i]
        return sum


s=Solution()
print(s.trap(height = [0,1,0,2,1,0,1,3,2,1,2,1]))
print(s.trap(height = [4,2,3]))

print(s.trap_fast(height = [0,1,0,2,1,0,1,3,2,1,2,1]))
print(s.trap_fast(height = [4,2,3]))