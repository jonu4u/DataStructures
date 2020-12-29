# 340. Longest Substring with At Most K Distinct Characters
#
# Given a string s and an integer k, return the length of the longest substring of s that contains at most k distinct characters.

# Example 1:
#
# Input: s = "eceba", k = 2
# Output: 3
# Explanation: The substring is "ece" with length 3.
# Example 2:
#
# Input: s = "aa", k = 1
# Output: 2
# Explanation: The substring is "aa" with length 2.
#
#
# Constraints:
#
# 1 <= s.length <= 5 * 104
# 0 <= k <= 50
class Solution(object):
    def lengthOfLongestSubstringKDistinct_sliding_set(self, s, k):
        if k==0:
            return 0
        tracker=set()
        size=len(s)
        left=0
        right=0
        max_length=0
        new_string=""
        while right<size:
            if len(tracker)<k:
                tracker.add(s[right])
                new_string+=s[right]
                right=right+1
                continue
            # comes here meaning tracker is at most k already. Now adding only if dups
            if s[right] in tracker:
                tracker.add(s[right])
                new_string+=s[right]
                right=right+1
            else:
                max_length=max(max_length,len(new_string))
                new_string=new_string[1:]
                if s[left] not in new_string and len(tracker)==k:
                    tracker.remove(s[left])
                left=left+1
        max_length=max(max_length,len(new_string))
        return max_length

    def lengthOfLongestSubstringKDistinct_sliding_hashmap(self, s, k):
        if k==0 or len(s)==0:
            return 0
        tracker={}
        left,right=0,0
        size=len(s)
        max_length=0
        while right<size:
            tracker[s[right]]=right
            right=right+1
            if len(tracker)==k+1:
                # Remove the leftmost element which is minimum index of values in map
                left_most_elem_idx=min(tracker.values())
                # Deletes the leftmost element from hashmap which can be picked by passing minimum index to the string
                del tracker[s[left_most_elem_idx]]
                # The number of charecters removed when we move the left element is the index of the left element +1
                # say in eceba index of e is 2.So if we remove e we're making left to jump to rightmost e. So we remove ece i.e index of e(2)+1=3 charecters
                left=left_most_elem_idx+1
            max_length=max(max_length,right-left)
        return max_length




s=Solution()
print(s.lengthOfLongestSubstringKDistinct_sliding_set("eceba", 2))
print(s.lengthOfLongestSubstringKDistinct_sliding_set("a", 0))
print(s.lengthOfLongestSubstringKDistinct_sliding_set("a", 1))
print(s.lengthOfLongestSubstringKDistinct_sliding_set("bacc", 2))
print("---------")
print(s.lengthOfLongestSubstringKDistinct_sliding_hashmap("eceba", 2))
print(s.lengthOfLongestSubstringKDistinct_sliding_hashmap("a", 0))
print(s.lengthOfLongestSubstringKDistinct_sliding_hashmap("a", 1))
print(s.lengthOfLongestSubstringKDistinct_sliding_hashmap("bacc", 2))
