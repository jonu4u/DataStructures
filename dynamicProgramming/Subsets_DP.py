# Print all subsets of a string/array
class Subsets_DP:
    def __init__(self):
        self.ans=[]
    def subset_rc(self,input,list1):
        if len(input)==0:
            self.ans.append(list1)
            return
        sub_list1=list1[:]
        sub_list2=list1[:]
        sub_list2.append(input[0])
        self.subset_rc(input[1:],sub_list1)
        self.subset_rc(input[1:],sub_list2)
        return

    def subset_sum_equal_k_rc(self, input, list1, target, sum):
        if len(input)==0:
            if sum==target:
                self.ans.append(list1)
            return
        sub_list1=list1[:]
        sub_list2=list1[:]
        sum1=sum
        sum2=sum+input[0]
        sub_list2.append(input[0])
        self.subset_sum_equal_k_rc(input[1:], sub_list1, target, sum1)
        self.subset_sum_equal_k_rc(input[1:], sub_list2, target, sum2)
        return

s=Subsets_DP()
s.subset_rc("abcd",[])
print(s.ans)

s=Subsets_DP()
s.subset_sum_equal_k_rc([1, 3, 4, 5, 2,7,8,13,21,23], [], 13, 0)
print(s.ans)

