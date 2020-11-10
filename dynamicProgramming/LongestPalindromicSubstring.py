# 5. Longest Palindromic Substring
#
# Given a string s, return the longest palindromic substring in s.
#
#
# Example 1:
#
# Input: s = "babad"
# Output: "bab"
# Note: "aba" is also a valid answer.
# Example 2:
#
# Input: s = "cbbd"
# Output: "bb"
# Example 3:
#
# Input: s = "a"
# Output: "a"
# Example 4:
#
# Input: s = "ac"
# Output: "a"
#
#
# Constraints:
#
# 1 <= s.length <= 1000
# s consist of only digits and English letters (lower-case and/or upper-case),
class Solution(object):
    def longestPalindrome(self, s):
        """
        :type s: str
        :rtype: str
        """
        reverse=list(s[:])
        reverse.reverse()
        reverse=''.join(reverse)
        if s in reverse:
            return s
        size=len(s)
        return self.longestCommonSubstring(s,reverse,size,size)


    def longestCommonSubstring(self,s1,s2,size1,size2):
        # Using Top down recursion
        memo=[["" for i in range(0,size1+1)] for i in range(0,size2+1)]
        ans=""
        for row in range(0,size1+1):
            for col in range(0,size2+1):
                # Base case
                if row==0 or col==0:
                    memo[row][col]=""
                elif s1[row-1]==s2[col-1]:
                    memo[row][col]=memo[row-1][col-1] + s1[row-1]
                    if self.is_palindrome(memo[row][col]):
                        ans=max([memo[row][col],ans],key=len)
                else:
                    memo[row][col]=""
        return ans

    def is_palindrome(self,string):
        size=len(string)
        left,right=0,size-1
        while left<right:
            if string[left]!=string[right]:
                return False
            left+=1
            right-=1
        return True


s=Solution()
# print(s.longestPalindrome("babad"))
# print(s.longestPalindrome("bb"))
print(s.longestPalindrome("ffffffffffffffffffffffffffffffffffffffffffffffffffffff"+
                          "ffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffff"+
                          "ffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffff"+
                          "ffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffff"+
                          "fffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffff"+
                          "ggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggg"+
                          "ggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggg"+
                          "ggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggg"+
                          "ggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggg"+
                          "gggggggggggggggggggggggggggggggggggggggggggggggggggggggggg"))