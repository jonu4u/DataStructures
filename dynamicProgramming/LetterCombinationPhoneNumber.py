# 17. Letter Combinations of a Phone Number
#
# Given a string containing digits from 2-9 inclusive, return all possible letter combinations that the number could represent. Return the answer in any order.
#
# A mapping of digit to letters (just like on the telephone buttons) is given below. Note that 1 does not map to any letters.
#
#
#
#
#
# Example 1:
#
# Input: digits = "23"
# Output: ["ad","ae","af","bd","be","bf","cd","ce","cf"]
# Example 2:
#
# Input: digits = ""
# Output: []
# Example 3:
#
# Input: digits = "2"
# Output: ["a","b","c"]
class Solution(object):
    def __init__(self):
        self.keypad_map={2:["a","b","c"],3:["d","e","f"],4:["g","h","i"],5:["j","k","l"],6:["m","n","o"],
                         7:["p","q","r""s"],8:["t","u","v"],9:["w","x","y","z"]}
    def letterCombinations(self, digits):
        """
        :type digits: str
        :rtype: List[str]
        """
        size=len(digits)
        if size==0:
            return digits
        if size==1:
            return self.keypad_map.get(int(digits))
        if size==2:
            return self.merge_two_digits(self.keypad_map.get(int(digits[0])),self.keypad_map.get(int(digits[1])),[],[])

        middle=size//2
        left=self.letterCombinations(digits[:middle+1])
        right=self.letterCombinations(digits[middle+1:])
        return self.merge_two_digits(left,right,[],[])


    def merge_two_digits(self,s1,s2,list1,list2):
        for char in s1:
            list1.extend(char)
            for char2 in s2:
                list1.extend(char2)
                list2.append(''.join(list1[:]))
                list1=list1[:len(list1)-len(char2)]
            list1=list1[:len(list1)-len(char)]
        return list2

s=Solution()
print(s.letterCombinations("234"))