# 438. Find All Anagrams in a String
#
# Given a string s and a non-empty string p, find all the start indices of p's anagrams in s.
#
# Strings consists of lowercase English letters only and the length of both strings s and p will not be larger than 20,100.
#
# The order of output does not matter.
#
# Example 1:
#
# Input:
# s: "cbaebabacd" p: "abc"
#
# Output:
# [0, 6]
#
# Explanation:
# The substring with start index = 0 is "cba", which is an anagram of "abc".
# The substring with start index = 6 is "bac", which is an anagram of "abc".
# Example 2:
#
# Input:
# s: "abab" p: "ab"
#
# Output:
# [0, 1, 2]
#
# Explanation:
# The substring with start index = 0 is "ab", which is an anagram of "ab".
# The substring with start index = 1 is "ba", which is an anagram of "ab".
# The substring with start index = 2 is "ab", which is an anagram of "ab".
class Solution(object):
    # This is getting TLE on leetcode for huge input as the sort algo is taking time
    def findAnagrams_naive(self, s, p):
        """
        :type s: str
        :type p: str
        :rtype: List[int]
        """
        left=0
        size=len(s)
        out=[]
        right=left+len(p)-1
        while right<size:
            substring=s[left:right+1]
            if self.is_anagram(substring):
                out.append(left)
            left+=1
            right=left+len(p)-1



    def is_anagram(self,string,p):
        if sorted(string)==sorted(p):
            return True
        return False

    # Using two hashmaps accepted by leetcode
    def findAnagrams_hashmap(self, s, p):
        """
        :type s: str
        :type p: str
        :rtype: List[int]
        """
        size=len(s)
        size_p=len(p)
        out=[]
        if size_p>size:
            return out
        if p==s:
            return out.append(0)
        p_map={}
        for elem in p:
            p_map[elem]=p_map.get(elem,0)+1
        s_map_till_p={}
        index=0
        while index<size_p:
            s_map_till_p[s[index]]=s_map_till_p.get(s[index],0)+1
            index+=1
        left=0
        right=left+size_p-1

        while right<size:
            if p_map==s_map_till_p:
                out.append(left)
            right+=1
            if right<size:
                s_map_till_p[s[right]]=s_map_till_p.get(s[right],0)+1
            s_map_till_p[s[left]]=s_map_till_p.get(s[left])-1
            if s_map_till_p[s[left]]==0:
                s_map_till_p.pop(s[left])
            left+=1
        return out

    # TAke an aray which contains count of elements from
    # 1-26 in 0-25 blocks.This is fastest.
    def findAnagrams_array_26_size(self, s, p):
        """
        :type s: str
        :type p: str
        :rtype: List[int]
        """
        size=len(s)
        size_p=len(p)
        out=[]
        if size_p>size:
            return out
        if p==s:
            return out.append(0)
        p_arr=[0 for i in range(0,128)]
        s_arr=[0 for i in range(0,128)]
        for elem in p:
            p_arr[ord(elem)]=p_arr[ord(elem)]+1


        left=0
        right=0
        ctr=0

        while right<size:
            s_arr[ord(s[right])]=s_arr[ord(s[right])]+1
            ctr+=1
            if ctr==size_p:
                ctr-=1
                if s_arr==p_arr:
                    out.append(left)
                s_arr[ord(s[left])]=s_arr[ord(s[left])]-1
                left+=1
            right+=1
        return out

# Same Problem
# 567. Permutation in String
#
# Given two strings s1 and s2, write a function to return true if s2 contains the permutation of s1. In other words, one of the first string's permutations is the substring of the second string.
#
#
#
# Example 1:
#
# Input: s1 = "ab" s2 = "eidbaooo"
# Output: True
# Explanation: s2 contains one permutation of s1 ("ba").
# Example 2:
#
# Input:s1= "ab" s2 = "eidboaoo"
# Output: False
