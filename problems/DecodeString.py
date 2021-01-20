# 394. Decode String
# Given an encoded string, return its decoded string.
#
# The encoding rule is: k[encoded_string], where the encoded_string inside the square brackets is being repeated exactly k times. Note that k is guaranteed to be a positive integer.
#
# You may assume that the input string is always valid; No extra white spaces, square brackets are well-formed, etc.
#
# Furthermore, you may assume that the original data does not contain any digits and that digits are only for those repeat numbers, k. For example, there won't be input like 3a or 2[4].
#
#
#
# Example 1:
#
# Input: s = "3[a]2[bc]"
# Output: "aaabcbc"
# Example 2:
#
# Input: s = "3[a2[c]]"
# Output: "accaccacc"
# Example 3:
#
# Input: s = "2[abc]3[cd]ef"
# Output: "abcabccdcdcdef"
# Example 4:
#
# Input: s = "abc3[cd]xyz"
# Output: "abccdcdcdxyz"
#
#
# Constraints:
#
# 1 <= s.length <= 30
# s consists of lowercase English letters, digits, and square brackets '[]'.
# s is guaranteed to be a valid input.
# All the integers in s are in the range [1, 300]
from collections import deque
class Solution(object):
    def decodeString(self, s):
        """
        :type s: str
        :rtype: str
        """
        out_str=self.decode_stack(s,"")
        # out_str=self.decode_nested(s,"")
        return out_str

    def decode_nested(self,ns,out):
        index=0
        sz=len(ns)
        # We loop thru the string to find an enclosing []. If we find that we recursively call that string inside bracket to decode
        while index<sz:
            # If the char is not number we continue and add this in the result
            if ns[index].isalpha():
                out+=ns[index]
                index+=1
                continue
            # If the charecter is number it means we have reached starting of a nested part
            if ns[index].isnumeric():
                number=ns[index]
                num_ind=index
                # The number can be more than 1 digit
                while ns[num_ind+1].isnumeric():
                    number+=ns[num_ind+1]
                    num_ind+=1
                # We find the nested substring inside bracket and recursively decode it
                string=self.find_nested_substring(ns[index+len(number):],0)
                out+=self.decode_nested(string,"")*int(number)
                index+=len(number)+2+len(string)
        return out

    def find_nested_substring(self,s,start_index):
        sz=len(s)
        bracket_ctr=0
        # We count opening and closing bracket.If both matches then we have found the complete nested string and return it
        # [2[e]t]--> nested string is 2[e]t for this.
        while start_index<sz:
            if s[start_index]=="[":
                bracket_ctr+=1
            elif s[start_index]=="]":
                bracket_ctr-=1

            if bracket_ctr==0:
                break
            start_index+=1
        return s[1:start_index]


    def decode_stack(self,ns,out):
        sz=len(ns)
        stack=deque()
        out=""
        index=0

        while index<sz:
            # If our charecter is not ] we push in stack:
            if ns[index]!=']':
                stack.appendleft(ns[index])
            else:
                # If we get a end bracket we pop the stack till [ comes.
                # When we reach a [ we try to find the number before it.Number can be more than one digit
                decode=""
                number=""
                while stack:
                    curr=stack.popleft()
                    if curr=="[":
                        continue
                    if curr.isalpha():
                        decode=curr+decode
                    elif curr.isnumeric():
                        number=curr+number
                        # We check next elem if exists.If its not a number we exit from this inner loop,
                        # we have got our string decode and number of times it needs to b decoded
                        if len(stack)>0:
                            next=stack.popleft()
                            if not next.isnumeric():
                                stack.appendleft(next)
                                break
                            stack.appendleft(next)
                decode=decode*int(number)
                # We put back the decoded string in top of stack
                stack.appendleft(decode)
            index+=1
        # Finally when our iteration complete we pop the elements and return out in reverse order we append
        while stack:
            elem=stack.popleft()
            out=elem+out
        return out


# s=Solution()
# print(s.decodeString("3[z]2[2[y]pq4[2[jk]e1[f]]]ef"))
# # 'zzzyypqjkjkefjkjkefjkjkefjkjkefyypqjkjkefjkjkefjkjkefjkjkefef'
# print(s.decodeString("3[a]2[bc]"))
# print(s.decodeString("2[abc]3[cd]ef"))
# print(s.decodeString("abc3[cd]xyz"))
# print(s.decodeString("3[a2[c]]"))
# print(s.decodeString("100[leetcode]"))
