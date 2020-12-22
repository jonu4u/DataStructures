# 264. Ugly Number II
#
# Write a program to find the n-th ugly number.
#
# Ugly numbers are positive numbers whose prime factors only include 2, 3, 5.
#
# Example:
#
# Input: n = 10
# Output: 12
# Explanation: 1, 2, 3, 4, 5, 6, 8, 9, 10, 12 is the sequence of the first 10 ugly numbers.
# Note:
#
# 1 is typically treated as an ugly number.
# n does not exceed 1690.
class Solution(object):
    def nthUglyNumber(self, n):
        """
        :type n: int
        :rtype: int
        """
        if n==1:
            return 1
        # Basically numbers which are multiples of 2 or 3 or 5 are ugly numbers.
        # Let's take an aray of n numbers to store ugly numbers
        ugly=[0]*n
        ugly[0]=1
        # Take three variables
        next_ugly_2=2
        next_ugly_3=3
        next_ugly_5=5
        i2=i3=i5=0
        for i in range(1,n):
            next_ugly=min(next_ugly_2,next_ugly_3,next_ugly_5)
            ugly[i]=next_ugly
            # Each time we get a ugly number, we increase the corresponding array index(i2/i3/i5)
            # and the next ugly is value at index * specific ugly i.e say i2=1
            # then next ugly =ugly[i2]*2=4
            # next ugly can be multiple. Like 6 can be next ugly of 2 as well as 3
            if next_ugly==next_ugly_2:
                i2+=1
                next_ugly_2=ugly[i2]*2
            if next_ugly==next_ugly_3:
                i3+=1
                next_ugly_3=ugly[i3]*3
            if next_ugly==next_ugly_5:
                i5+=1
                next_ugly_5=ugly[i5]*5
        return ugly[n-1]
# 313. Super Ugly Number
# Write a program to find the nth super ugly number.
#
# Super ugly numbers are positive numbers whose all prime factors are in the given prime list primes of size k.
#
# Example:
#
# Input: n = 12, primes = [2,7,13,19]
# Output: 32
# Explanation: [1,2,4,7,8,13,14,16,19,26,28,32] is the sequence of the first 12
# super ugly numbers given primes = [2,7,13,19] of size 4.
# Note:
#
# 1 is a super ugly number for any given primes.
# The given numbers in primes are in ascending order.
# 0 < k ≤ 100, 0 < n ≤ 106, 0 < primes[i] < 1000.
# The nth super ugly number is guaranteed to fit in a 32-bit signed integer.
    def nthSuperUglyNumber(self, n, primes):
        """
        :type n: int
        :type primes: List[int]
        :rtype: int
        """
        # Take a map to keep track of iterator for each prime
        primes_map={i:0 for i in primes}
        # This map taks care of next ugly for each prime
        next_ugly_map={i:i for i in primes}
        ugly=[0]*n
        ugly[0]=1
        for i in range(1,n):
            next_ugly=min(next_ugly_map.values())
            ugly[i]=next_ugly
            for key,value in next_ugly_map.items():
                # We need to update the prime map as well
                # as next ugly map with latest values
                if value==next_ugly:
                    primes_map[key]=primes_map.get(key)+1
                    # This is the ith ugly index * key
                    next_ugly_map[key]=ugly[primes_map.get(key)]*key
        return ugly[n-1]

s=Solution()
print(s.nthUglyNumber(10))
print(s.nthSuperUglyNumber(12,[2,7,13,19]))
# The space complexity is O(n+number of primes)==O(N)