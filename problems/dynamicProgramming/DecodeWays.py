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
        self.decode_memo_rc("",str(int(s)),[])
        return self.ans

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

    # def decode_memo_rc(self,left_char,remaining,ctr,original_length):
    def decode_memo_rc(self,left_char,remaining,list1):
        # if ctr==original_length:
        #     self.ans.append(''.join(list1))
        #     return list1
        if len(left_char)>0 and left_char not in self.letter_map:
            return list1
        else:
            list1.append(self.letter_map.get(left_char))
        if remaining==0:
            # self.ans.append(''.join(list1))
            # return list1
            list1.append(self.letter_map.get(left_char))
            return list1

        one_char=self.decode_memo_rc(remaining[0],remaining[1:],list1)
        two_char=self.decode_memo_rc(remaining[0:2],remaining[2:],list1)
        # if string in self.memo:
        #     list1.append(self.memo.get(string))
        #     ctr=ctr-len(self.memo.get(string))
        #     return list1
        # self.memo[string]=''.join(list1)
        # for index,elem in enumerate(string):
        #     if index+1<len(string):
        #         if elem==0:
        #             ctr+=1
        #             continue
        #         if self.letter_map.get(elem):
        #             list1.append(self.letter_map.get(elem))
        #             ctr+=1
        #             list1=self.decode_memo_rc(string[1:],list1,ctr,original_length)
        #             # self.memo[string]=''.join(list1[len(list1)-len(string):])
        #             list1.pop(len(list1)-1)
        #             ctr-=1
        #         if self.letter_map.get(string[0:2]):
        #             list1.append(self.letter_map.get(string[0:2]))
        #             ctr+=2
        #             list1=self.decode_memo_rc(string[2:],list1,ctr,original_length)
        #             # self.memo[string]=list1.pop(len(list1)-1)
        #             list1.pop(len(list1)-1)
        #             ctr-=2
        #     else:
        #         if self.letter_map.get(elem):
        #             list1.append(self.letter_map.get(elem))
        #             ctr+=1
        #             list1=self.decode_memo_rc(string[1:],list1,ctr,original_length)
        #             # self.memo[string]=''.join(list1[len(list1)-len(string):])
        #             list1.pop(len(list1)-1)
        #             ctr-=1
        #     ctr-=1
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



# s=Solution()
# # Trim all leading zeroes before sending
# # s.numDecodings("123123")
# s.numDecodings("123")
# print(s.ans)

list=[1,2,3]
list[0],list[2]=list[2]+1,list[0]
print(list)


