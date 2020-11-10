class Solution:
    def __init__(self,size=10000):
        self.ans=""
        # Max length given in constrainsts
        self.memoizize_rc=[]

    # Recursion + Memoizize
    def LCS_RC_Memozize(self, s1, s2, size1, size2):
        # Base Case
        if size1==0 or size2==0:
            return self.memoizize_rc[size1][size2]
        if self.memoizize_rc[size1][size2]!="":
            return self.memoizize_rc[size1][size2]
        # Choice Diagram
        if s1[size1-1]==s2[size2-1]:
            self.memoizize_rc[size1][size2]= self.LCS_RC_Memozize(s1, s2, size1 - 1, size2 - 1)+s1[size1-1]
            return self.memoizize_rc[size1][size2]
        left=self.LCS_RC_Memozize(s1, s2, size1 - 1, size2)
        right=self.LCS_RC_Memozize(s1, s2, size1, size2 - 1)
        max_string=max([left,right],key=len)
        self.memoizize_rc[size1][size2]=max_string
        return self.memoizize_rc[size1][size2]

    def LCS_top_down(self,s1,s2,size1,size2):
        memo=[["" for i in range(0, 100)] for i in range(0, 100)]
        for row in range(0,size1+1):
            for col in range(0,size2+1):
                if row==0 or col==0:
                    memo[row][col]=""
                elif s1[row-1]==s2[col-1]:
                    memo[row][col]=memo[row-1][col-1] + s1[row-1]
                else:
                    memo[row][col]=max([memo[row][col-1],memo[row-1][col]],key=len)
        return memo[size1][size2]






s=Solution()
s.memoizize_rc=[["" for i in range(0, 13)] for i in range(0, 13)]
print(s.LCS_RC_Memozize("bacabab", "babacab", 7, 7))
s.memoizize_rc=[["" for i in range(0, 13)] for i in range(0, 13)]
print(s.LCS_RC_Memozize("aacabdkacaa", "aacakdbacaa", 11, 11))

print(s.LCS_top_down("bacabab", "babacab", 7, 7))
print(s.LCS_top_down("aacabdkacaa", "aacakdbacaa", 11, 11))