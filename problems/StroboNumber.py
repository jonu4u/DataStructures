# 246. Strobogrammatic Number
#
# A strobogrammatic number is a number that looks the same when rotated 180 degrees (looked at upside down).
#
# Write a function to determine if a number is strobogrammatic. The number is represented as a string.
#
#
#
# Example 1:
#
# Input: num = "69"
# Output: true
# Example 2:
#
# Input: num = "88"
# Output: true
# Example 3:
#
# Input: num = "962"
# Output: false
# Example 4:
#
# Input: num = "1"
# Output: true
class Solution(object):
    def isStrobogrammatic(self, num):
        """
        :type num: str
        :rtype: bool
        """
        symmetry_map={"1":"1","6":"9","8":"8","9":"6","0":"0"}
        new=""
        for elem in num:
            if elem in symmetry_map:
                new=symmetry_map[elem]+new
            else:
                return False
        if new==num:
            return True
        return False

# 247. Strobogrammatic Number II
#
# A strobogrammatic number is a number that looks the same when rotated 180 degrees (looked at upside down).
#
# Find all strobogrammatic numbers that are of length = n.
#
# Example:
#
# Input:  n = 2
# Output: ["11","69","88","96"]

    # In this solution we have to jump numbers when they are not in symmetry map
    # This causes TLE in Leetcode when n=10
    def findStrobogrammatic(self, n):
        """
        :type n: int
        :rtype: List[str]
        """
        symmetry_map={"1":"1","6":"9","8":"8","9":"6","0":"0"}
        out=[]
        start=0
        if n>1:
            start=10**(n-1)
        while start <10**n:
            # When the first char is not in the map we jump 10^n-1 numbers
            if str(start)[0] in symmetry_map:
                start,is_strob=self.is_strob(str(start),symmetry_map,start)
                if is_strob:
                    out.append(str(start-1))
            else:
                if str(start)[0]=="2":
                   start=start+(10**(n-1))*4
                else:
                   start=start+10**(n-1)
        return out



    def is_strob(self,num,symmetry_map,loop_ctr):
        new=""
        for index,elem in enumerate(num):
            if elem not in symmetry_map:
                # When any char is not in the map we jump 10**(len(num)-index-1)) numbers
                # If the elem is 2 we can straightaway jump 2,3,4,5
                if elem=="2":
                    loop_ctr=loop_ctr+(10**(len(num)-index-1))*4
                # When the number is odd the middle number can only contain 0 or 1
                # to be strob so we skip 2-9 here
                elif len(num)%2!=0 and elem==num[len(num)//2] and elem==2:
                    loop_ctr=loop_ctr+(10**(len(num)-index-1))*8
                else:
                    loop_ctr=loop_ctr+(10**(len(num)-index-1))
                return (loop_ctr,False)
            else:
                new=symmetry_map[elem]+new
        if new==num:
            return (loop_ctr+1,True)
        return (loop_ctr+1,False)

    # We have to write more effficient way of checking is_strob
    # Start from middle if it contains 6 then next must be 9.Then fan out and it should have either
    #     of symmetry numbers in between or outside
    def is_strob_eff(self,num,symmetry_map,loop_ctr):
        new=""
        for index,elem in enumerate(num):
            if elem not in symmetry_map:
                # When any char is not in the map we jump 10**(len(num)-index-1)) numbers
                # If the elem is 2 we can straightaway jump 2,3,4,5
                if elem=="2":
                    loop_ctr=loop_ctr+(10**(len(num)-index-1))*4
                else:
                    loop_ctr=loop_ctr+(10**(len(num)-index-1))
                return (loop_ctr,False)
            else:
                new=symmetry_map[elem]+new
        if new==num:
            return (loop_ctr+1,True)
        return (loop_ctr+1,False)


s=Solution()
# print(10**0)
from datetime import datetime
print(datetime.now())
print(s.findStrobogrammatic(9))
print(datetime.now())

