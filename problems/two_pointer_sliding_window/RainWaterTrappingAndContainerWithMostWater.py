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

# 11. Container With Most Water
# Given n non-negative integers a1, a2, ..., an , where each represents a point at coordinate (i, ai). n vertical lines are drawn such that the two endpoints of the line i is at (i, ai) and (i, 0). Find two lines, which, together with the x-axis forms a container, such that the container contains the most water.
#
# Notice that you may not slant the container.
#
# Example 1:
#
#
# Input: height = [1,8,6,2,5,4,8,3,7]
# Output: 49
# Explanation: The above vertical lines are represented by array [1,8,6,2,5,4,8,3,7]. In this case, the max area of water (blue section) the container can contain is 49.
# Example 2:
#
# Input: height = [1,1]
# Output: 1
# Example 3:
#
# Input: height = [4,3,2,1,4]
# Output: 16
# Example 4:
#
# Input: height = [1,2,1]
# Output: 2
#
#
# Constraints:
#
# n = height.length
# 2 <= n <= 3 * 104
# 0 <= height[i] <= 3 * 104
class Solution(object):
    def maxArea(self, height):
        """
        :type height: List[int]
        :rtype: int
        """
        return self.maxArea_smart(height)

    # Results in TLE
    def maxArea_brute(self,height):
        max_area=float('-inf')
        left=0
        size=len(height)
        while left<size-1:
            right=left+1
            while right<size:
                area=min(height[left],height[right])*(right-left)
                max_area=max(max_area,area)
                right+=1
            left+=1
        return max_area
    # The trick here is take a pointer at begin and end
    # and move pointer inward for whichever height is lower.
    # The lower height dictates the area.
    # The assumption is the lower height may have a higher height adjacent to it which will
    # compensate the reduce in width and could give max area.
    # https://leetcode.com/problems/container-with-most-water/solution/
    def maxArea_smart(self,height):
        max_area=float('-inf')
        left=0
        right=len(height)-1
        while left<right:
            area=min(height[left],height[right])*(right-left)
            max_area=max(max_area,area)
            if height[left]>height[right]:
                right-=1
            else:
                left+=1
        return max_area