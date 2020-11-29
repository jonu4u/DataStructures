# 139. Word Break
#
# Given a non-empty string s and a dictionary wordDict containing a list of non-empty words, determine if s can be segmented into a space-separated sequence of one or more dictionary words.
#
# Note:
#
# The same word in the dictionary may be reused multiple times in the segmentation.
# You may assume the dictionary does not contain duplicate words.
# Example 1:
#
# Input: s = "leetcode", wordDict = ["leet", "code"]
# Output: true
# Explanation: Return true because "leetcode" can be segmented as "leet code".
# Example 2:
#
# Input: s = "applepenapple", wordDict = ["apple", "pen"]
# Output: true
# Explanation: Return true because "applepenapple" can be segmented as "apple pen apple".
# Note that you are allowed to reuse a dictionary word.
# Example 3:
#
# Input: s = "catsandog", wordDict = ["cats", "dog", "sand", "and", "cat"]
# Output: false
class Solution(object):
    def wordBreak(self, s, wordDict):
        """
        :type s: str
        :type wordDict: List[str]
        :rtype: bool
        """
        # return self.word_break_rc(s,set(wordDict),0)
        memo=[None for i in range(0,len(s)+1)]
        return self.word_break_rc_memo(s,set(wordDict),0,memo)

    def word_break_rc(self,s,wordSet,start_index):
        if start_index==len(s)-1:
            if s in wordSet:
                return True
            else:
                return False

        for i in range(start_index,len(s)+1):
            initial_word=s[:start_index+1]
            if initial_word not in wordSet:
                return self.word_break_rc(s,wordSet,start_index+1)
            else:
                return True and (self.word_break_rc(s[start_index+1:],wordSet,0) or self.word_break_rc(s,wordSet,start_index+1))

    def word_break_rc_memo(self,s,wordSet,start_index,memo):
        # When the index reaches the length it means no more char left
        if start_index==len(s):
                return True

        if memo[start_index] is not None:
            return memo[start_index]

        # Check for start_index to start+1 if a word can be formed
        for i in range(start_index+1,len(s)+1):
            initial_word=s[start_index:i]
            # If we can form a valid word, we continue with the rest of the string to
            # see if a valid word can be formed. If not we continue on the for loop and
            #     add more charecters to the initial word
            if initial_word in wordSet and self.word_break_rc_memo(s,wordSet,i,memo):
                memo[start_index]= True
                return memo[start_index]
        memo[start_index]=False
        return memo[start_index]

s=Solution()
print(s.wordBreak(s = "applepenapple", wordDict = ["apple", "pen"]))
print(s.wordBreak(s = "catsandog", wordDict = ["cats", "dog", "sand", "and", "cat"]))
print(s.wordBreak(s = "cars", wordDict = ["car", "ca", "rs"]))
print(s.wordBreak(s = "aaaaaaa", wordDict = ["aaaa", "aaa"]))

