# 350. Intersection of Two Arrays II
#
# Given two arrays, write a function to compute their intersection.
#
# Example 1:
#
# Input: nums1 = [1,2,2,1], nums2 = [2,2]
# Output: [2,2]
# Example 2:
#
# Input: nums1 = [4,9,5], nums2 = [9,4,9,8,4]
# Output: [4,9]
# Note:
#
# Each element in the result should appear as many times as it shows in both arrays.
# The result can be in any order.
# Follow up:
#
# What if the given array is already sorted? How would you optimize your algorithm?
# What if nums1's size is small compared to nums2's size? Which algorithm is better?
# What if elements of nums2 are stored on disk, and the memory is limited such that you cannot load all elements into the memory at once?
class Solution(object):
    # One solution is to create a hashmap from the bigger array and then find each element from smaller array in it
    def intersect_map(self, nums1, nums2):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :rtype: List[int]
        """
        size1=len(nums1)
        size2=len(nums2)
        greater=nums1
        lesser=nums2
        if size2>size1:
            greater=nums2
            lesser=nums1
        char_map={}
        out=[]
        for elem in greater:
            char_map[elem]=char_map.get(elem,0)+1
        for elem in lesser:
            if elem in char_map:
                out.append(elem)
                if char_map[elem]==1:
                    char_map.pop(elem)
                else:
                    char_map[elem]=char_map[elem]-1
        return out

    # Another solution is to use binary search in bigger array to find small one
    # but it'll be slower than hashmap approach which is O(N)':
