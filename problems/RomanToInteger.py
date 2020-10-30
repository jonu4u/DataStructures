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