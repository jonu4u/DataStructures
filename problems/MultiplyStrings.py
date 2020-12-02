# 43. Multiply Strings
#
# Given two non-negative integers num1 and num2 represented as strings, return the product of num1 and num2, also represented as a string.
#
# Note: You must not use any built-in BigInteger library or convert the inputs to integer directly.
#
# Example 1:
#
# Input: num1 = "2", num2 = "3"
# Output: "6"
# Example 2:
#
# Input: num1 = "123", num2 = "456"
# Output: "56088"
#
#
# Constraints:
#
# 1 <= num1.length, num2.length <= 200
# num1 and num2 consist of digits only.
# Both num1 and num2 do not contain any leading zero, except the number 0 itself.
class Solution(object):
    def multiply_smart(self, num1, num2):
        if num1=="0" or num2=="0":
            return "0"
        int1=self.create_int_from_string(num1)
        int2=self.create_int_from_string(num2)
        return str(int1*int2)

    def create_int_from_string(self,num):
        power=len(num)-1
        sum=0
        for char in num:
            # Now a digit can be from 0-9
            for i in range(0,10):
                if str(i)==char:
                    sum=sum+i*(10**power)
                    power-=1
        return sum




s=Solution()
print(s.create_int_from_string("987654321"))
print(s.multiply_smart("123456789", "987654321"))



