# 32. Longest Valid Parentheses
#
# Given a string containing just the characters '(' and ')', find the length of the longest valid (well-formed) parentheses substring.
#
#
#
# Example 1:
#
# Input: s = "(()"
# Output: 2
# Explanation: The longest valid parentheses substring is "()".
# Example 2:
#
# Input: s = ")()())"
# Output: 4
# Explanation: The longest valid parentheses substring is "()()".
# Example 3:
#
# Input: s = ""
# Output: 0
#
#
# Constraints:
#
# 0 <= s.length <= 3 * 104
# s[i] is '(', or ')'.
from collections import deque
class Solution(object):
#
# Instead of finding every possible string and checking its validity, we can make use of stack while scanning the given string to check if the string scanned so far is valid, and also the length of the longest valid string. In order to do so, we start by pushing -1−1 onto the stack.
#
# For every \text{‘(’}‘(’ encountered, we push its index onto the stack.
#
#                   For every \text{‘)’}‘)’ encountered, we pop the topmost element and subtract the current element's index from the top element of the stack, which gives the length of the currently encountered valid string of parentheses. If while popping the element, the stack becomes empty, we push the current element's index onto the stack. In this way, we keep on calculating the lengths of the valid substrings, and return the length of the longest valid string at the end.
#
# See this example for better understanding.
# https://leetcode.com/problems/longest-valid-parentheses/solution/
    from collections import deque
    def longestValidParentheses(self, s):
        """
        :type s: str
        :rtype: int
        """
        size=len(s)
        if size==0:
            return 0
        q=deque()
        q.appendleft(-1)
        max_len=0
        for index,char in enumerate(s):
            if char==')':
                q.popleft()
                if len(q)>0:
                    prev=q.popleft()
                    length=index-prev
                    max_len=max(length,max_len)
                    q.appendleft(prev)
                else:
                    q.appendleft(index)
            else:
                q.appendleft(index)
        return max_len

















