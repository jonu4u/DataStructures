class Solution(object):
    def romanToInt(self, s):
        roman_map={"I":1,"V":5,"X":10,"L":50,"C":100,"D":500,"M":1000,"IV":4,"IX":9,"XL":40,"XC":90,"CD":400,"CM":900}
        index=0
        sum=0
        while index<len(s):
           two_digits= roman_map.get(s[index:index+2])
           if two_digits is not None:
               sum+=two_digits
               index+=2
           else:
               sum+=roman_map.get(s[index])
               index+=1
        return sum


s=Solution()
print(s.romanToInt("MCMXCIV"))
print(s.romanToInt("III"))

# 12. Integer to Roman
# Roman numerals are represented by seven different symbols: I, V, X, L, C, D and M.
#
# Symbol       Value
# I             1
# V             5
# X             10
# L             50
# C             100
# D             500
# M             1000
# For example, 2 is written as II in Roman numeral, just two one's added together. 12 is written as XII, which is simply X + II. The number 27 is written as XXVII, which is XX + V + II.
#
# Roman numerals are usually written largest to smallest from left to right. However, the numeral for four is not IIII. Instead, the number four is written as IV. Because the one is before the five we subtract it making four. The same principle applies to the number nine, which is written as IX. There are six instances where subtraction is used:
#
# I can be placed before V (5) and X (10) to make 4 and 9.
# X can be placed before L (50) and C (100) to make 40 and 90.
# C can be placed before D (500) and M (1000) to make 400 and 900.
# Given an integer, convert it to a roman numeral.
#
#
#
# Example 1:
#
# Input: num = 3
# Output: "III"
# Example 2:
#
# Input: num = 4
# Output: "IV"
# Example 3:
#
# Input: num = 9
# Output: "IX"
# Example 4:
#
# Input: num = 58
# Output: "LVIII"
# Explanation: L = 50, V = 5, III = 3.
# Example 5:
#
# Input: num = 1994
# Output: "MCMXCIV"
# Explanation: M = 1000, CM = 900, XC = 90 and IV = 4.
#
#
# Constraints:
#
# 1 <= num <= 3999
from collections import OrderedDict
class Solution(object):
    def intToRoman_naive(self, num):
        """
        :type num: int
        :rtype: str
        """
        int_map=OrderedDict([(1000,"M"),(500,"D"),(100,"C"),(50,"L"),(10,"X"),(5,"V"),(1,"I")])
        exception_map={4:"IV",9:"IX",40:"XL",90:"XC",400:"CD",900:"CM"}
        roman=""
        left=0
        num=str(num)
        size=len(num)
        while left<size:
            mult=size-left
            digit=int(num[left])*(10**(mult-1))
            # We want to extract the 1000s,100s,10s and units. Say 2531.
            # So we take 2000,500,30 and 1 as steps.Then we figure out the
            # corresponding romans from them and append
            if digit in int_map:
                roman+=int_map[digit]
            elif digit in exception_map:
                roman+=exception_map[digit]
            else:
                roman+=self.derive_number(digit,int_map)
            left+=1
        return roman

    def derive_number(self,digit,map):
        out=""
        for key,value in map.items():
            if key<=digit:
                quotient,remainder=divmod(digit,key)
                out+=map[key]*quotient
                digit=remainder
                if digit==0:
                    break
        return out

    # Here we take max possible key while we can
    # and subtract key from number
    def intToRoman_greedy(self, num):
        """
        :type num: int
        :rtype: str
        """
        int_map=OrderedDict([(1000,"M"),(900,"CM"),(500,"D"),(400,"CD"),(100,"C"),(90,"XC"),(50,"L"),(40,"XL"),(10,"X"),(9,"IX"),(5,"V"),(4,"IV"),(1,"I")])
        roman=""
        for key,value in int_map.items():
            if key>num:
                continue
            while key<=num:
                roman+=value
                num=num-key
            if num==0:
                break
        return roman
