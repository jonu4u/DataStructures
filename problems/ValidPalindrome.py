# 680. Valid Palindrome II
#
# Given a non-empty string s, you may delete at most one character. Judge whether you can make it a palindrome.
#
# Example 1:
# Input: "aba"
# Output: True
# Example 2:
# Input: "abca"
# Output: True
# Explanation: You could delete the character 'c'.
# Note:
# The string will only contain lowercase characters a-z. The maximum length of the string is 50000.
class Solution(object):
    def validPalindrome(self, s):
        """
        :type s: str
        :rtype: bool
        """
        size=len(s)
        left=0
        right=size-1
        # we start from begin and end
        while left<right:
            # when begin and end matches we continue
            if s[left]==s[right]:
                left+=1
                right-=1
                continue
            # when we reach middle and there is no match only in middle we can skip one letter
            # so return True
            if right-left==1:
                return True
            # In all other cases we take left+1 to right or left to right-1 and check if these strings are palindromes
            return self.is_palindrome(s[left+1:right+1]) or self.is_palindrome(s[left:right])
        # If we come out of while it's a palindrome so we retun True'
        return True

    # Whenever any of the left and right don't match we say false'
    def is_palindrome(self,s):
        left=0
        right=len(s)-1
        while left<right:
            if s[left]!=s[right]:
                return False
            left+=1
            right-=1
        return True