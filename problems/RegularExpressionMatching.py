# 10. Regular Expression Matching
#
# Given an input string (s) and a pattern (p), implement regular expression matching with support for '.' and '*' where:
#
# '.' Matches any single character.​​​​
# '*' Matches zero or more of the preceding element.
# The matching should cover the entire input string (not partial).
#
#
#
# Example 1:
#
# Input: s = "aa", p = "a"
# Output: false
# Explanation: "a" does not match the entire string "aa".
# Example 2:
#
# Input: s = "aa", p = "a*"
# Output: true
# Explanation: '*' means zero or more of the preceding element, 'a'. Therefore, by repeating 'a' once, it becomes "aa".
# Example 3:
#
# Input: s = "ab", p = ".*"
# Output: true
# Explanation: ".*" means "zero or more (*) of any character (.)".
# Example 4:
#
# Input: s = "aab", p = "c*a*b"
# Output: true
# Explanation: c can be repeated 0 times, a can be repeated 1 time. Therefore, it matches "aab".
# Example 5:
#
# Input: s = "mississippi", p = "mis*is*p*."
# Output: false
#
#
# Constraints:
#
# 0 <= s.length <= 20
# 0 <= p.length <= 30
# s contains only lowercase English letters.
# p contains only lowercase English letters, '.', and '*'.
# It is guaranteed for each appearance of the character '*', there will be a previous valid character to match.
from collections import OrderedDict
class Solution(object):
    def isMatch(self, s, p):
        """
        :type s: str
        :type p: str
        :rtype: bool
        """
        # Intuitive is to do two loops
        if p==".*" or s==p:
            return True
        size_match=len(p)
        char_s=""
        for index,char in enumerate(p):
            if char=="*":
                continue
            if len(s)>0:
                char_s=s[0]
            elif len(s)==0 and char==char_s and p[index-1]=="*":
                continue
            elif index+1<size_match and p[index+1]=="*":
                continue
            elif len(s)==0:
                return False
            if index+1<size_match and char!="." and p[index+1] != "*" and char_s!=char:
                    return False
            elif index+1<size_match and (char_s==char or char==".") and p[index+1] == "*":
                for i in s:
                    if i==char_s:
                        s=s[1:]
                    else:
                        break
            elif char=="." or char_s==char:
                s=s[1:]
            elif index+1<size_match and p[index+1] == "*" and char_s!=char:
                    continue


        if len(s)==0:
            return True
        return False

s=Solution()
print(s.isMatch("mississippi",  "mis*is*p*."))
print(s.isMatch("mississippi",  "mis*is*.p*."))
print(s.isMatch("mississippi",  "mis*i*c*d*f*s*.p*."))
print(s.isMatch("aaa", "aaaa"))
print(s.isMatch("aaa","ab*a*c*a"))
print(s.isMatch("a","ab*"))







