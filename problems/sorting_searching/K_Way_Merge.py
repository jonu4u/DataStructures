# Given a list of k lists merge using k way merge
import heapq as hq
class Solution:
    def merge(self,lists):
        master_list=[]
        for l in lists:
            master_list.append((l[0],(l,0)))
        hq.heapify(master_list)
        out=[]
        while len(master_list)>0:
            elem,arr_tuple=hq.heappop(master_list)
            out.append(elem)
            arr,index=arr_tuple
            if index+1<len(arr):
               master_list.append((arr[index+1],(arr,index+1)))
               hq.heapify(master_list)

        return out

s=Solution()
l=[[0,2,4],
   [1,2,2,2,6,8],
   [0,3,5,7],
   [5,10],
   [9,10,11,12,13]
]
print(s.merge(l))



