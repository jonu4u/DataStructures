# 953. Verifying an Alien Dictionary
#
# In an alien language, surprisingly they also use english lowercase letters, but possibly in a different order. The order of the alphabet is some permutation of lowercase letters.
#
# Given a sequence of words written in the alien language, and the order of the alphabet, return true if and only if the given words are sorted lexicographicaly in this alien language.
#
#
#
# Example 1:
#
# Input: words = ["hello","leetcode"], order = "hlabcdefgijkmnopqrstuvwxyz"
# Output: true
# Explanation: As 'h' comes before 'l' in this language, then the sequence is sorted.
# Example 2:
#
# Input: words = ["word","world","row"], order = "worldabcefghijkmnpqstuvxyz"
# Output: false
# Explanation: As 'd' comes after 'l' in this language, then words[0] > words[1], hence the sequence is unsorted.
# Example 3:
#
# Input: words = ["apple","app"], order = "abcdefghijklmnopqrstuvwxyz"
# Output: false
# Explanation: The first three characters "app" match, and the second string is shorter (in size.) According to lexicographical rules "apple" > "app", because 'l' > '∅', where '∅' is defined as the blank character which is less than any other character (More info).
#
#
# Constraints:
#
# 1 <= words.length <= 100
# 1 <= words[i].length <= 20
# order.length == 26
# All characters in words[i] and order are English lowercase letters.
class Solution(object):
    def __init__(self):
        self.letter_map={}
    def isAlienSorted(self, words, order):
        """
        :type words: List[str]
        :type order: str
        :rtype: bool
        """
        index=1
        size=len(words)
        if size==1:
            return True
        for elem in order:
            self.letter_map[elem]=index
            index+=1
        for ctr,word in enumerate(words):
            if ctr+1<size:
                first_char_first=self.letter_map.get(word[0])
                first_char_second=self.letter_map.get(words[ctr+1][0])
                if first_char_first>first_char_second:
                    return False
                elif first_char_first==first_char_second:
                    compare=self.compare_words(word,words[ctr+1])
                    if compare==-1:
                        return False
        return True


    def compare_words(self,word1,word2):
        min_len=min(len(word1),len(word2))
        char_first=0
        char_second=0
        for i in range(0,min_len):
            char_first=self.letter_map.get(word1[i])
            char_second=self.letter_map.get(word2[i])
            if char_first>char_second:
                return -1

        if char_first==char_second:
            if len(word1)>len(word2):
                return -1
        return 0