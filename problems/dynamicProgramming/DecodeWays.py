class Solution:
    def __init__(self):
        self.ans=[]
        self.memo={}
        self.letter_map={"1":"A","2":"B","3":"C","4":"D","5":"E","6":"F","7":"G","8":"H","9":"I","10":"J","11":"K","12":"L","13":"M","14":"N","15":"O","16":"P","17":"Q","18":"R","19":"S","20":"T","21":"U","22":"V","23":"W","24":"X","25":"Y","26":"Z"}
    def numDecodings(self, s):
        """
        :type s: str
        :rtype: int
        """
        return self.decode_memo_recursive_memo(s,0)

    def decode(self,string,list1,ctr,original_length):
        if ctr==original_length:
            self.ans.append(''.join(list1))
            return list1
        for index,elem in enumerate(string):
            if index+1<len(string):
                    if elem==0:
                        ctr+=1
                        continue
                    if self.letter_map.get(elem):
                        list1.append(self.letter_map.get(elem))
                        ctr+=1
                        list1=self.decode(string[1:],list1,ctr,original_length)
                        list1.pop(len(list1)-1)
                        ctr-=1
                    if self.letter_map.get(string[0:2]):
                        list1.append(self.letter_map.get(string[0:2]))
                        ctr+=2
                        list1=self.decode(string[2:],list1,ctr,original_length)
                        # self.memo[string[2:]]=''.join(list1)
                        list1.pop(len(list1)-2)
                        ctr-=2
            else:
                if self.letter_map.get(elem):
                    list1.append(self.letter_map.get(elem))
                    ctr+=1
                    list1=self.decode(string[1:],list1,ctr,original_length)
                    list1.pop(len(list1)-1)
                    ctr-=1
            ctr-=1
        return list1


    # This is the final solution of leetcode
    def decode_memo_recursive_memo(self,decode_str,index):
        # It means we have reached end of string so return 1, base condition
        if index==len(decode_str):
            return 1
        # If we encounter a 0 we don't decode'
        if decode_str[index]=='0':
            return 0

        # For two digit decoding if there are two chars left then also we return
        if index==len(decode_str)-1:
            return 1

        if index in self.memo:
            return self.memo.get(index)

        ans = self.decode_memo_recursive_memo(decode_str,index+1)  + \
              (self.decode_memo_recursive_memo(decode_str,index+2) if (int(decode_str[index : index+2]) <= 26) else 0)

        self.memo[index]=ans

        return ans


        # return list1



s=Solution()
# Trim all leading zeroes before sending
s.numDecodings("123123")
s.numDecodings("123")
print(s.ans)



