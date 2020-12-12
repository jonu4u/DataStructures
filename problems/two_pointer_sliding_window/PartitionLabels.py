# IMPORTANT Amazon
# 763. Partition Labels
#
# A string S of lowercase English letters is given. We want to partition this string into as many parts as possible so that each letter appears in at most one part, and return a list of integers representing the size of these parts.
#
#
#
# Example 1:
#
# Input: S = "ababcbacadefegdehijhklij"
# Output: [9,7,8]
# Explanation:
# The partition is "ababcbaca", "defegde", "hijhklij".
# This is a partition so that each letter appears in at most one part.
# A partition like "ababcbacadefegde", "hijhklij" is incorrect, because it splits S into less parts.
#
#
# Note:
#
# S will have length in range [1, 500].
# S will consist of lowercase English letters ('a' to 'z') only.
class Solution(object):
    def partitionLabels(self, S):
        """
        :type S: str
        :rtype: List[int]
        """
        # We take a count of each letter in the string
        letter_map={}
        for char in S:
            letter_map[char]=letter_map.get(char,0)+1
        # We take a set to take care of distinct letters
        distinct_letter=set()
        # We take a counter to count len of substring,
        # we we want the actual substrings we could have taken the string but
        # only length is reqd
        ctr=0
        out=[]
        for i,char in enumerate(S):
            # We take one charecter and add it to substring as well
            # as distinct char and reduce the count of that char from map
            ctr+=1
            distinct_letter.add(char)
            letter_map[char]-=1
            # If there is no letter left of this char,
            # we pop this char and remove this element from distinct set
            if letter_map[char]==0:
                letter_map.pop(char)
                distinct_letter.remove(char)
            # If there are no more chars in distinct set, it means we can take
            # a substring now as all distinct chars in that segment are exhausted
            if len(distinct_letter)==0:
                out.append(ctr)
                # We reset the length of substring
                ctr=0
        return out