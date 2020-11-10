class Solution:
    def __init__(self,size=10000):
        self.ans=""
        # Max length given in constrainsts
        self.memoizize_rc=self.memoizize_top_down=[["" for i in range(0, 13)] for i in range(0, 13)]

    # Recursion + Memoizize
    def LCS_RC_Memozize(self, s1, s2, size1, size2):
        # Base Case
        if size1==0 or size2==0:
            return self.memoizize_rc[size1][size2]
        if self.memoizize_rc[size1][size2]!="":
            return self.memoizize_rc[size1][size2]
        # Choice Diagram
        if s1[size1-1]==s2[size2-1]:
            self.memoizize_rc[size1][size2]= s1[size1-1] + self.LCS_RC_Memozize(s1, s2, size1 - 1, size2 - 1)
            return self.memoizize_rc[size1][size2]
        left=self.LCS_RC_Memozize(s1, s2, size1 - 1, size2)
        right=self.LCS_RC_Memozize(s1, s2, size1, size2 - 1)
        max_string=max([left,right],key=len)
        self.memoizize_rc[size1][size2]=max_string
        return self.memoizize_rc[size1][size2]




s=Solution()
print(s.LCS_RC_Memozize("bacabab", "babacab", 7, 7))
print(s.LCS_RC_Memozize("aacabdkacaa", "aacakdbacaa", 11, 11))