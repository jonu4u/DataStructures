# 46. Permutations
#
# Given a collection of distinct integers, return all possible permutations.
#
# Example:
#
# Input: [1,2,3]
# Output:
# [
#     [1,2,3],
#     [1,3,2],
#     [2,1,3],
#     [2,3,1],
#     [3,1,2],
#     [3,2,1]
# ]

class Solution(object):
    def __init__(self):
        self.ans=[]
    def permute(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        size=len(nums)
        if size<2:
            return [nums]
        self.permutation(nums,[],size)
        return self.ans

    def permutation(self,nums,list1,size):
        # When list1 size equals actual size we append it to result
        if len(list1)==size:
            self.ans.append(list1[:])
            return list1
        for index,char in enumerate(nums):
            list1.append(char)
            list1=self.permutation(nums[0:index]+nums[index+1:],list1,size)
            list1=list1[:len(list1)-1]
        return list1

    def permutation_unique(self,nums,list1,size):
        # When list1 size equals actual size we append it to result
        if len(list1)==size and list1 not in self.ans:
            self.ans.append(list1[:])
            return list1
        for index,char in enumerate(nums):
            list1.append(char)
            list1=self.permutation(nums[0:index]+nums[index+1:],list1,size)
            list1=list1[:len(list1)-1]
        return list1

s=Solution()
