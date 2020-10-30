class Solution(object):
    def lengthOfLongestSubstring_brute(self, s):
        if(len(s)==1):
            return 1
        newString=""
        max_length=0
        for index,sub in enumerate(s):
            if index+1==len(s):
                newString+=s
                break
            inner_sbstr=s[index+1:len(s)]
            newString+=sub
            for j,sub2 in enumerate(inner_sbstr):
                if sub2 not in newString:
                    newString+=sub2
                else:
                    break
            max_length=max(max_length,len(newString))
            newString=""
        return max_length

    def lengthOfLongestSubstring_sliding_window(self,s):
        left=0
        right=0
        max_len=0
        unique=set()
        while right<len(s):
            if s[right] not in unique:
                unique.update(s[right])
                right+=1
                max_len=max(max_len,len(unique))
            else:
                unique.remove(s[left])
                left+=1
        return max_len





s=Solution()
print(s.lengthOfLongestSubstring_brute("au"))
print(s.lengthOfLongestSubstring_brute("bbbb"))
print(s.lengthOfLongestSubstring_brute("pwwkew"))
print(s.lengthOfLongestSubstring_brute("abcabcbb"))
print(s.lengthOfLongestSubstring_brute(" "))
print("--------------")
print(s.lengthOfLongestSubstring_sliding_window("au"))
print(s.lengthOfLongestSubstring_sliding_window("bbbb"))
print(s.lengthOfLongestSubstring_sliding_window("pwwkew"))
print(s.lengthOfLongestSubstring_sliding_window("abcabcbb"))
print(s.lengthOfLongestSubstring_sliding_window(" "))
