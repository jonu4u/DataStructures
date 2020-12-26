# 22. Generate Parentheses
#
# Given n pairs of parentheses, write a function to generate all combinations of well-formed parentheses.
#
#
#
# Example 1:
#
# Input: n = 3
# Output: ["((()))","(()())","(())()","()(())","()()()"]
# Example 2:
#
# Input: n = 1
# Output: ["()"]
#
#
# Constraints:
#
# 1 <= n <= 8
class Solution(object):
    def generateParenthesis(self, n):
        """
        :type n: int
        :rtype: List[str]
        """
        out=[]
        self.recursive(n,n,"",out)
        return out
    # We have a open bracket and close bracket count
    def recursive(self,open,close,output,out_list):
        # When both open and close bracket is 0 we have complrted our string and put that in result list
        if (open == 0 and close == 0):
            out_list.append(output)
            return
        # If we have open bracket left we can choose it anytime and do recursion
        if open!=0:
            op1=output
            op1+="("
            self.recursive(open-1,close,op1,out_list)
        # We can only take a close bracket when close bracket count is more than open else we'll have'
        # non balanced string'
        if close>open:
            op2=output
            op2+=")"
            self.recursive(open,close-1,op2,out_list)
        return

s=Solution()
s.generateParenthesis(3)