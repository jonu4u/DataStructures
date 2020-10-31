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

    def threeSumClosest(self, nums, target):
        nums=sorted(tuple(nums))
        dups=set()
        outer_index=0
        size=len(nums)
        closest_positive=999999999
        closest_negative=-99999999
        while outer_index<size-2:
            if nums[outer_index] not in dups:
                dups.add(nums[outer_index])
                first_num=nums[outer_index]
                left=outer_index+1
                right=size-1
                while left<right:
                    sum=first_num+nums[left]+nums[right]
                    diff = sum-target
                    if diff==0 :
                        return target
                    elif diff>0:
                        right=right-1
                        closest_positive=min(closest_positive,diff)
                    elif diff<0:
                        left=left+1
                        closest_negative=max(closest_negative,diff)
            outer_index+=1
        if abs(closest_positive)>abs(closest_negative):
            return target+ closest_negative
        else:
            return target + closest_positive

s=Solution()
# print(s.threeSum_brute([-1,0,1,2,-1,-4]))
print(s.threeSum_brute([-1,0,1,2,-1,-4,-2,-3,3,0,4]))
print(s.threeSum_brute2([-1,0,1,2,-1,-4,-2,-3,3,0,4]))
print(s.threeSum_set([-1,0,1,2,-1,-4,-2,-3,3,0,4]))
# [[-4,0,4],[-4,1,3],[-3,-1,4],[-3,0,3],[-3,1,2],[-2,-1,3],[-2,0,2],[-1,-1,2],[-1,0,1]]
# print(s.threeSum_brute([]))
# print(s.threeSum_brute([0]))

print(s.threeSumClosest([1,1,-1,-1,3],
                        -1))