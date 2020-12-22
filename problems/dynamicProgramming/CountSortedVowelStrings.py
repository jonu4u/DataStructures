# 1641. Count Sorted Vowel Strings

# Given an integer n, return the number of strings of length n that consist only of vowels (a, e, i, o, u) and are lexicographically sorted.
#
# A string s is lexicographically sorted if for all valid i, s[i] is the same as or comes before s[i+1] in the alphabet.
#
#
#
# Example 1:
#
# Input: n = 1
# Output: 5
# Explanation: The 5 sorted strings that consist of vowels only are ["a","e","i","o","u"].
# Example 2:
#
# Input: n = 2
# Output: 15
# Explanation: The 15 sorted strings that consist of vowels only are
# ["aa","ae","ai","ao","au","ee","ei","eo","eu","ii","io","iu","oo","ou","uu"].
# Note that "ea" is not a valid string since 'e' comes after 'a' in the alphabet.
# Example 3:
#
# Input: n = 33
# Output: 66045

class Solution(object):
    def countVowelStrings(self, n):
        """
        :type n: int
        :rtype: int
        """
        vowels=["a","e","i","o","u"]
        # The vowels can be changed as well as n
        dp=[[0]*(n+1)]*6
        for row in range(1,6):
            for col in range(1,n+1):
                # When vowel is 1 whatever is n result is always 1
                if row==1:
                    dp[row][col]=1
                # When n=1 it is equal to number of vowels i.e row number
                elif col==1:
                    dp[row][col]=row
                else:
                    # This is the main code and I saw it from solution,
                    # couldn't figure this out
                    dp[row][col]=dp[row-1][col]+dp[row][col-1]
        return dp[5][n]