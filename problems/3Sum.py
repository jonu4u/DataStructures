class Solution(object):
    def threeSum_brute(self, nums):
        # sort the list
        nums=sorted(tuple(nums))
        unique=[]
        # Take the 1st element of nums
        target=0
        # Take two pointers left from target+1 and right =last
        while target<len(nums)-2:
            if target>0 and nums[target]==nums[target-1]:
                target+=1
                continue
            first_number=nums[target]
            left=target+1
            right=len(nums)-1
            while left<right:
                sum=first_number+nums[left]+nums[right]
                if sum>0:
                    right=right-1
                elif sum<0:
                    left=left+1
                elif sum==0:
                    unique.append([first_number,nums[left],nums[right]])
                    left=left+1
                    right=right-1
            target+=1
        return unique

    def threeSum_set(self, nums):
        unique=set()
        dups,seen=set(),{}
        for i,elem1 in enumerate(nums):
            if elem1 not in dups:
                dups.add(elem1)
                for j,elem2 in enumerate(nums[i+1:]):
                    complement= -elem1 - elem2
                    if complement in seen and seen[complement]==i:
                        unique.add(tuple(sorted((elem2,elem1,complement))))
                    seen[elem2]=i
        return unique

    # In this approach I used a set to skip dups. Also the return can be set of tuples
    def threeSum_brute2(self, nums):
        # sort the list
        nums=sorted(tuple(nums))
        unique=set()
        # Take the 1st element of nums
        target=0
        dups=set()
        # Take two pointers left from target+1 and right =last
        while target<len(nums)-2:
            # we check if the value is not a duplicate
            if nums[target] not in dups:
                dups.add(nums[target])
                first_number=nums[target]
                left=target+1
                right=len(nums)-1
                while left<right:
                    sum=first_number+nums[left]+nums[right]
                    if sum>0:
                        right=right-1
                    elif sum<0:
                        left=left+1
                    elif sum==0:
                        list=(first_number,nums[left],nums[right])
                        unique.add(list)
                        left=left+1
                        right=right-1
            target+=1
        return unique


s=Solution()
# print(s.threeSum_brute([-1,0,1,2,-1,-4]))
print(s.threeSum_brute([-1,0,1,2,-1,-4,-2,-3,3,0,4]))
print(s.threeSum_brute2([-1,0,1,2,-1,-4,-2,-3,3,0,4]))
print(s.threeSum_set([-1,0,1,2,-1,-4,-2,-3,3,0,4]))
# [[-4,0,4],[-4,1,3],[-3,-1,4],[-3,0,3],[-3,1,2],[-2,-1,3],[-2,0,2],[-1,-1,2],[-1,0,1]]
# print(s.threeSum_brute([]))
# print(s.threeSum_brute([0]))