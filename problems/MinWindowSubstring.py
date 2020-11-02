# 76. Minimum Window Substring
#
# Given two strings s and t, return the minimum window in s which will contain all the characters in t. If there is no such window in s that covers all characters in t, return the empty string "".
#
# Note that If there is such a window, it is guaranteed that there will always be only one unique minimum window in s.
#
#
#
# Example 1:
#
# Input: s = "ADOBECODEBANC", t = "ABC"
# Output: "BANC"
# Example 2:
#
# Input: s = "a", t = "a"
# Output: "a"
#
#
# Constraints:
#
# 1 <= s.length, t.length <= 105
# s and t consist of English letters.
from collections import Counter
class Solution(object):
    def minWindow_naive(self, s, t):
        if len(t)>len(s):
            return ""
        # Counter returns a map of chars and their occurences from a string,
        # but counter is not efficient
        # actual_map=Counter(t)
        actual_map={}
        for char in t:
            actual_map[char]=actual_map.get(char,0)+1
        min_length=999999999999
        left,right=0,0
        new_map={}
        desired_window=""
        min_window=""
        while right<len(s)+1:
            if len(new_map)==len(actual_map) and self.is_desired_window(actual_map,new_map):
                 if len(desired_window)<min_length:
                     min_window=desired_window
                     min_length=len(desired_window)
                 desired_window=desired_window[1:]
                 self.remove_from_map(s[left],new_map)
                 left+=1
            else:
                if right<len(s):
                    if s[right] in actual_map:
                      new_map[s[right]]=new_map.get(s[right],0)+1
                    desired_window+=s[right]
                right+=1
        return min_window

    def remove_from_map(self,value,new_map):
        if new_map.get(value) is not None:
                if new_map.get(value) ==1:
                    new_map.pop(value)
                else:
                    new_map[value]=new_map.get(value)-1

    def is_desired_window(self,actual_map,new_map):
        count=len(actual_map)
        for k in actual_map.keys():
            if new_map.get(k)>=actual_map.get(k):
                count-=1
        if count==0:
            return True
        return False

    def minWindow(self, s, t):
        if len(t)>len(s):
            return ""
        # Counter returns a map of chars and their occurences from a string,
        # but counter is not efficient
        # actual_map=Counter(t)
        actual_map={}
        for char in t:
            actual_map[char]=actual_map.get(char,0)+1
        actual_distinct_charecters_in_substring=len(actual_map)
        distinct_desired_charecter_count=0
        left,right=0,0
        window_map={}
        is_substring_in_string=False
        # tuple of left pointer,right pointer,size of window
        min_window=(0,0,99999999999)
        while right<len(s):
            charecter=s[right]
            # We add each charecter to the window_map and if exists increase the counter
            window_map[charecter]=window_map.get(charecter,0)+1
            # When a charecter is in the substring(actual_map) we check if the occurences of that charecter also match ,
            # if yes then we increase counter of distinct charecters
            if charecter in actual_map and window_map[charecter]==actual_map.get(charecter):
                distinct_desired_charecter_count+=1

            # if the desired unique charecters is reached ,Contract the window from left and check if the window is still desirable
            if distinct_desired_charecter_count==actual_distinct_charecters_in_substring:
                # If any char of substring is in string then this is true
                is_substring_in_string=True
                # replace the left,right pointers and the length of the window when window length is minimum
                if min_window[2]>(right-left+1):
                    min_window=(left,right,right-left+1)
                # We start reducing the window, i.e removing charecters from left till the right-1 index is reached
                while left<right:
                    left_char=s[left]
                    # We remove the entry accordingly from the map and if the element kength becomes 0 in map remove the element altogether
                    window_map[left_char]=window_map.get(left_char)-1
                    if window_map[left_char]==0:
                        window_map.pop(left_char)
                    # We check after each contraction that the current window is still desirable or not
                    # by checking if the charecter removed is one in the substring and if the
                    # occurences match that in the substring.
                    #  We break from conract if window is not desirable
                    if left_char in actual_map and window_map.get(left_char,0)<actual_map[left_char]:
                        # We reduce the distinct count by one
                        distinct_desired_charecter_count-=1
                        # we check what the minimum window is again
                        if min_window[2]>(right-left+1):
                            min_window=(left,right,right-left+1)
                        # we increase the left counter and break
                        left+=1
                        break
                    left+=1
            # Again we expand the window to further right to create a desirable window and so on
            right+=1
        # Edge cases: if both are null return empty, if substring > string return empty,
        #     if length of substring is one and substring is in strinmg return substring.
        # For all other cases return the substring from left to right+1
        if is_substring_in_string and len(t)>1:
            return s[min_window[0]:min_window[1]+1]
        elif is_substring_in_string and len(t)==1:
            return t
        else:
            return ""


s=Solution()
print(s.minWindow("babb","baba"))
print(s.minWindow("ADOBECODEBANC","ABC"))
print(s.minWindow("a","a"))
print(s.minWindow("a","aa"))
print(s.minWindow("a","b"))
print(s.minWindow("abc","bc"))
print(s.minWindow("abc","c"))
print(s.minWindow("ab","b"))
print(s.minWindow("aaa","aa"))
print(s.minWindow("abc","cba"))
print(s.minWindow("cabwefgewcwaefgcf","cae"))










