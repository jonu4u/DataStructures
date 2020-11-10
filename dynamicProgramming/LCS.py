class Solution:
    def __init__(self,size=10000):
        self.ans=""
        self.memoizize=[]

    def LCS(self,s1,s2,size1,size2,common):
        # Base Case
        if size1==0 or size2==0:
            return common
        # Choice Diagram
        c2=common
        if s1[size1-1]==s2[size2-1]:
            c2= self.LCS(s1,s2,size1-1,size2-1,common+s1[size1-1])
        left=self.LCS(s1,s2,size1-1,size2,"")
        right=self.LCS(s1,s2,size1,size2-1,"")
        max_string=max([c2,left,right],key=len)
        return max_string

    def LCS_1(self,s1,s2,size1,size2):
        # Base Case
        self.memoizize=[["" for i in range(0,size1+1)]for i in range(0,size2+1)]
        self.ans=""
        for row in range(0,size1+1):
            for col in range(0,size2+1):
                if row==0 or col==0:
                    self.memoizize[row][col]=""

                # Choice Diagram
                elif s1[row-1]==s2[col-1]:
                    self.memoizize[row][col]=self.memoizize[row-1][col-1]+s1[row-1]
                    if self.is_palindrome(self.memoizize[row][col]):
                        self.ans=max([self.memoizize[row][col],self.ans],key=len)
                else:
                    self.memoizize[row][col]=""
        return self.ans

    def is_palindrome(self,string):
        reverse=list(string[:])
        reverse.reverse()
        reverse=''.join(reverse)
        if string == reverse:
            return True
        return False


s=Solution()
print(s.LCS_1("bacabab","babacab",7,7))
print(s.LCS_1("aacabdkacaa","aacakdbacaa",11,11))
