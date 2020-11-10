class Solution(object):
    def longestPalindrome(self, s):
        """
        :type s: str
        :rtype: str
        """
        if len(s)<2:
            return s
        start=0
        end=0
        for i,elem in enumerate(s):
            len1=self.expand_from_center(s,i,i)
            len2=self.expand_from_center(s,i,i+1)
            str_len=max(len1,len2)
            if str_len>end-start:
                start=i-((str_len-1)/2)
                end=i+(str_len/2)
        return s[start:end+1]

    def expand_from_center(self,s,left,right):
        if left<0 or left>right:
            return 0
        while (left>=0 and right<len(s) and s[left]==s[right]):
            left-=1
            right+=1
        return right - left -1

    def longestPalindrome_naive(self, s):
        """
        :type s: str
        :rtype: str
        """
        reverse=list(s[:])
        reverse.reverse()
        reverse=''.join(reverse)
        if s in reverse:
            return s
        size=len(s)
        return self.longestCommonSubstring(s,reverse,size,size)


    def longestCommonSubstring(self,s1,s2,size1,size2):
        # Using Top down recursion
        memo=[["" for i in range(0,size1+1)] for i in range(0,size2+1)]
        ans=""
        for row in range(0,size1+1):
            for col in range(0,size2+1):
                # Base case
                if row==0 or col==0:
                    memo[row][col]=""
                elif s1[row-1]==s2[col-1]:
                    memo[row][col]=memo[row-1][col-1] + s1[row-1]
                    if self.is_palindrome(memo[row][col]):
                        ans=max([memo[row][col],ans],key=len)
                else:
                    memo[row][col]=""
        return ans

    def is_palindrome(self,string):
        size=len(string)
        left,right=0,size-1
        while left<right:
            if string[left]!=string[right]:
                return False
            left+=1
            right-=1
        return True