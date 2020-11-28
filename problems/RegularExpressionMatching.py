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
class Solution(object):
    def isMatch(self, s, p):
        """
        :type s: str
        :type p: str
        :rtype: bool
        """
        memo = {}
        # We start with 0th element of text and pattern
        def dp(i, j):
            if (i, j) not in memo:
                # if both have length 0 ten True else False
                if j == len(p):
                    ans = (i==len(s))
                else:
                    # If the first charecter matches text in pattern or it is '.'
                    # then it's a match
                    first_match = i < len(s) and p[j] in {s[i], '.'}
                    # If we have two chars and the 2nd char is '*'
                    # it could be a match or we can ignore this
                    if j+1 < len(p) and p[j+1] == '*':
                              # This is when we ignore or
                              # This is when we match both charecters
                        ans = dp(i, j+2) \
                              or first_match and dp(i+1, j)
                    else:
                        ans = first_match and dp(i+1, j+1)

                memo[i, j] = ans
            return memo[i, j]

        return dp(0, 0)

s=Solution()
print(s.isMatch("mississippi",  "mis*is*p*."))
print(s.isMatch("mississippi",  "mis*is*.p*."))
print(s.isMatch("mississippi",  "mis*i*c*d*f*s*.p*."))
print(s.isMatch("aaa", "aaaa"))
print(s.isMatch("aaa","ab*a*c*a"))
print(s.isMatch("a","ab*"))
print(s.isMatch("a","ab*a"))
print(s.isMatch("ab",".*.."))







