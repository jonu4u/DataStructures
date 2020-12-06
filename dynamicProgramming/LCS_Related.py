class LCS:
#     Longest Common Subsequence Problem solution using recursion
# Given two sequences, find the length of longest subsequence present in both of them.
# A subsequence is a sequence that appears in the same relative order, but not necessarily contiguous.
#
# For example, “abc”,  “abg”, “bdf”, “aeg”,  ‘”acefg”, .. etc are subsequences of “abcdefg”.
    def __init__(self):
        self.memo=[]

    def LCS_memo_rc(self,s1,s2,size1,size2):
        if size1==0 or size2==0:
            return self.memo[size1][size2]

        if self.memo[size1][size2]!="":
            return self.memo[size1][size2]

        if s1[size1-1]==s2[size2-1]:
            # When we have match from both end we append string as cureent string and
            # put rest of the string in recursion
            self.memo[size1][size2]=self.LCS_memo_rc(s1,s2,size1-1,size2-1) + s1[size1-1]
            return self.memo[size1][size2]

        # If end char not matches then we take end-1 from 1 string
        # and end-1 from next string. We take max string out of these as current memeoized cell
        left=self.LCS_memo_rc(s1,s2,size1-1,size2)
        right=self.LCS_memo_rc(s1,s2,size1,size2-1)
        self.memo[size1][size2]=max([left,right],key=len)
        return self.memo[size1][size2]

    def LCS_top_down(self,s1,s2,size1,size2):
        dp=[["" for i in range(0,size1+1)]for i in range(0,size2+1)]
        for row in range(0,size2+1):
            for col in range(0,size1+1):
                if row==0 or col==0:
                    dp[row][col]=""
                elif s1[col-1]==s2[row-1]:
                    dp[row][col]=dp[row-1][col-1]+s1[col-1]
                else:
                    dp[row][col]=max([dp[row-1][col],dp[row][col-1]],key=len)
        return dp[size2][size1]

    # Longest Common Substring(Dynamic Programming)
    # Given two strings ‘X’ and ‘Y’, find the length of the longest common substring.
    # Examples:
    #
    # Input : X = “GeeksforGeeks”, y = “GeeksQuiz”
    # Output : 5
    # The longest common substring is “Geeks” and is of length 5.
    def LCSubstring_top_down(self,s1,s2,size1,size2):
        dp=[["" for i in range(0,size1+1)]for i in range(0,size2+1)]
        ans=""
        for row in range(0,size2+1):
            for col in range(0,size1+1):
                if row==0 or col==0:
                    dp[row][col]=""
                elif s1[col-1]==s2[row-1]:
                    dp[row][col]=dp[row-1][col-1]+s1[col-1]
                    ans=max([ans,dp[row][col]],key=len)
                else:
                    # Whenever the chars don't match we start afresh
                    dp[row][col]=""
        return ans

    # Minimum number of deletions and insertions to transform one string into another
    # Given two strings ‘str1’ and ‘str2’ of size m and n respectively. The task is to remove/delete and insert minimum number of characters from/in str1 so as to transform it into str2. It could be possible that the same character needs to be removed/deleted from one point of str1 and inserted to some another point.
    # Example:
    # Input : str1 = "geeksforgeeks", str2 = "geeks"
    # Output : Minimum Deletion = 8
    # Minimum Insertion = 0
    def min_insert_delete(self,s1,s2):
        size1=len(s1)
        size2=len(s2)
        lcs=self.LCS_top_down(s1,s2,size1,size2)
        # The minimum changes are from 1st string length - lcs number of deletions
        # from 2nd string -lcs number of insertions
        return (size1-len(lcs))+(size2-len(lcs))

    # 72. Edit Distance !!!!IMP 
    #
    # Given two strings word1 and word2, return the minimum number of operations required to convert word1 to word2.
    #
    # You have the following three operations permitted on a word:
    #
    # Insert a character
    # Delete a character
    # Replace a character
    #
    #
    # Example 1:
    #
    # Input: word1 = "horse", word2 = "ros"
    # Output: 3
    # Explanation:
    # horse -> rorse (replace 'h' with 'r')
    # rorse -> rose (remove 'r')
    # rose -> ros (remove 'e')
    # Example 2:
    #
    # Input: word1 = "intention", word2 = "execution"
    # Output: 5
    # Explanation:
    # intention -> inention (remove 't')
    # inention -> enention (replace 'i' with 'e')
    # enention -> exention (replace 'n' with 'x')
    # exention -> exection (replace 'n' with 'c')
    # exection -> execution (insert 'u')
    def edit_distance(self,word1,word2):
        size1=len(word1)
        size2=len(word2)
        dp=[[0 for i in range(0,size2+1)] for i in range(0,size1+1)]
        for row in range(size1+1):
            for col in range(size2+1):
                # When row is 0 i.e one string is zero the other string is simply equal
                # to length of that string needed for edit
                if row==0:
                    dp[row][col]=col
                elif col==0:
                    dp[row][col]=row
                elif word1[row-1]==word2[col-1]:
                    # This is same as diagonal as it remains unchanged
                    dp[row][col]=dp[row-1][col-1]
                else:
                    # When end charecter not matches ,
                    # so we take min of left col, up row and diag row col
                    # and add the current operation as 1
                    #                   insert,     delete,       replace
                    # Draw the table to find out why or check youtube
                    dp[row][col]=min(dp[row][col-1],dp[row-1][col],dp[row-1][col-1])+1
        return dp[size1][size2]





# Shortest Common Supersequence
    # Given two strings str1 and str2, find the shortest string that has both str1 and str2 as subsequences.
    # Examples:
    #
    # Input:   str1 = "geek",  str2 = "eke"
    # Output: "geeke"
    # def shortest_common_supersequence(self,s1,s2,size1,size2):
    #     lcs=self.LCS_top_down(s1,s2,size1,size2)
    #     if len(lcs)==0:
    #         return s1+s2




s=LCS()
s.memo=[["" for i in range(0, 13)] for i in range(0, 13)]
print(s.LCS_memo_rc("bacabab", "babacab", 7, 7))
s.memo=[["" for i in range(0, 13)] for i in range(0, 13)]
print(s.LCS_memo_rc("aacabdkacaa", "aacakdbacaa", 11, 11))

print(s.LCS_top_down("bacabab", "babacab", 7, 7))
print(s.LCS_top_down("aacabdkacaa", "aacakdbacaa", 11, 11))


print(s.LCSubstring_top_down("bacabab", "babacab", 7, 7))
print(s.LCSubstring_top_down("aacabdkacaa", "aacakdbacaa", 11, 11))
