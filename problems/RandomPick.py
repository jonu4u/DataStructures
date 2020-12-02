# 398. Random Pick Index
#
# Given an array of integers with possible duplicates, randomly output the index of a given target number. You can assume that the given target number must exist in the array.
#
# Note:
# The array size can be very large. Solution that uses too much extra space will not pass the judge.
#
# Example:
#
# int[] nums = new int[] {1,2,3,3,3};
# Solution solution = new Solution(nums);
#
# // pick(3) should return either index 2, 3, or 4 randomly. Each index should have equal probability of returning.
# solution.pick(3);
#
# // pick(1) should return 0. Since in the array only nums[0] is equal to 1.
# solution.pick(1);
import random
class Solution(object):

    def __init_naive__(self, nums):
        """
        :type nums: List[int]
        """
        self.nums=nums


    # This works better
    def pick_naive(self, target):
        """
        :type target: int
        :rtype: int
        """
        dup=[]
        # Brute is to search array for target and store the indices
        for index,elem in enumerate(self.nums):
            if elem==target:
                dup.append(index)
        return random.choice(dup)

    def __init__(self, nums):
        """
        :type nums: List[int]
        """
        # create a hashmap and precompute all indices in one pass
        self.map={}
        for index,elem in enumerate(self.nums):
            if not self.map.get(elem):
                self.map[elem]=[index]
            else:
                self.map.get(elem).append(index)


    def pick(self, target):
        """
        :type target: int
        :rtype: int
        """
        return random.choice(self.map.get(target))

