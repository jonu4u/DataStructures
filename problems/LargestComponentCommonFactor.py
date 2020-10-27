# 952.LeetCode:  Largest Component Size by Common Factor
# Given a non-empty array of unique positive integers A, consider the following graph:
#
# There are A.length nodes, labelled A[0] to A[A.length - 1];
# There is an edge between A[i] and A[j] if and only if A[i] and A[j] share a common factor greater than 1.
# Return the size of the largest connected component in the graph.
#
#
#
# Example 1:
#
# Input: [4,6,15,35]
# Output: 4
#
# Example 2:
#
# Input: [20,50,9,63]
# Output: 2
#
# Example 3:
#
# Input: [2,3,6,7,4,12,21,39]
# Output: 8
#
# Note:
#
# 1 <= A.length <= 20000
# 1 <= A[i] <= 100000

import math
# The below solution works but slow so not accepted by leetcode
class Solution(object):
    def largestComponentSize(self, A):
        graph=UnionFind()
        for elem in A:
            if len(graph.is_visited)==len(A):
                break
            for elem1 in A:
                if elem1==elem:
                    continue
                if elem1 in graph.is_visited and elem in graph.is_visited:
                    continue
                if graph.has_common_factor(elem,elem1):
                    graph.addEdge(elem,elem1)
                    graph.union(elem,elem1)

        return graph.max_val

    def prime_factors(self,num):
        prime_factors=set()
        if num % 2 == 0:
            prime_factors.add(2)

        for i in range(3, int(math.sqrt(num))+1, 2):
            if num % i == 0:
                prime_factors.add(i)
        return prime_factors




class UnionFind:
    def __init__(self):
        self.parent={}
        self.index=0
        self.graph=[]
        self.max_val=-1
        self.is_visited=set()

    def __add_vertex(self,V):
        self.parent[self.index]=[V]
        self.index+=1


    def addEdge(self,u,v):
        self.graph.append((u,v))
        is_u_present = False
        is_v_present = False
        for valueList in self.parent.values():
            if u in valueList:
                is_u_present=True
            if v in valueList:
                is_v_present=True
        if not is_u_present:
            self.__add_vertex(u)
        if not is_v_present:
            self.__add_vertex(v)

    # u is >v
    def has_common_factor(self,u,v):
        if u<v:
           u,v=v,u
        for i in range(2,u):
            if(i>v):
                break
            if (u % i)==0 and (v % i)==0:
                return True

        return False

    def findParent(self,value):
        for key,valueList in self.parent.items():
            if value in valueList:
                return key

    def union(self,u,v):
        parent1=self.findParent(u)
        parent2=self.findParent(v)
        if parent1== parent2:
            return

        size1=len(self.parent.get(parent1))
        size2=len(self.parent.get(parent2))
        if size1>size2:
            self.combine_groups(parent1,parent2)
        else:
            self.combine_groups(parent2,parent1)


    def combine_groups(self,key1,key2):
        # In a python dict remember just get the value and do whatever u want on it. No need to assign it again to key.
        # self.parent[key1]=self.parent.get(key1).extend(self.parent.get(key2))  This is wrong and don't work
         valueList1=self.parent.get(key1)
         valueList1.extend(self.parent.get(key2))
         self.parent.pop(key2)
         self.max_val=max(self.max_val,len(valueList1))



s= Solution()
# print(s.prime_factors(242))
print(s.largestComponentSize([4,6,15,35]))
print(s.largestComponentSize([20,50,9,63]))
print(s.largestComponentSize([2,3,6,7,4,12,21,39]))
print(s.largestComponentSize([100,68,70,79,80,20,25,27]))
print(s.largestComponentSize([99,100,69,39,14,56,91,60]))
from datetime import datetime
print(datetime.now())
print(s.largestComponentSize([5803,6153,13,2062,6161,2068,7172,8219,6174,2080,36,4138,6188,8237,46,8240,8242,4151,6202,8253,8269,2126,6226,2135,4187,97,102,9233,6263,126,3776,2178,4233,8330,9581,8342,152,6297,5487,4253,8350,2208,6308,4262,4263,6314,1053,8373,184,4281,2242,8388,6346,6352,2258,6355,2261,2084,4815,6365,2270,225,4330,4333,6525,4341,6390,3455,4355,262,8456,6410,2318,6873,4379,6435,297,2439,302,2364,2372,334,4431,2387,340,8590,345,2400,8548,6508,367,4466,371,6516,2429,2662,391,2442,8589,398,8595,2452,4506,415,2467,8612,8615,4525,6578,8627,4535,2489,445,4542,447,8644,4558,629,6611,4567,6564,6620,4582,6638,496,4596,2549,4605,513,6660,8714,4620,2579,2585,6685,544,4644,557,8816,6717,8767,6723,2628,582,4679,3853,4689,2643,599,4700,614,8807,618,4882,6768,626,4724,2677,2689,642,4740,6790,4749,158,8848,5913,4769,2724,2730,4779,8897,717,2206,719,2769,8916,6871,4825,2788,8934,6890,751,6898,4855,2811,8960,4915,8967,4877,786,2835,2843,2848,6945,2851,8997,2856,6958,6961,9011,9012,9014,6976,4931,4932,842,7309,4947,9046,7001,2910,9055,2917,1169,7017,874,7655,9072,2931,9078,2935,9024,7044,9103,912,9105,923,5021,7071,1520,5029,2982,5033,2987,7089,7667,2997,950,7533,7096,954,6033,5059,970,9719,973,3023,1669,5075,3034,2895,5084,9181,7141,7142,3050,9196,7150,9201,1015,5116,9220,9223,3083,1036,1041,175,7197,1055,1057,3108,3109,7212,3123,5173,7223,1081,7007,1085,3143,9293,5424,5205,1893,7266,1128,9325,1146,1157,5258,9357,1166,9361,7325,9385,9392,7346,3254,1208,5309,9412,9416,5321,1229,7374,1238,5339,9436,5344,1254,9451,5368,3326,5376,1282,2945,3341,3343,7440,7441,1298,3348,5397,5398,3351,3633,5416,7465,3975,1325,3376,1335,3385,9536,7492,5445,3399,3402,3408,5462,9559,9934,5474,1383,3437,7535,9593,9597,1406,5503,7555,5511,3464,1423,7568,7570,3651,7573,3481,1437,7589,3496,9649,5559,9665,1474,7627,1487,7632,1495,5592,9126,3558,593,7657,9708,3568,5618,595,3575,5625,3583,1536,1537,5634,9131,7685,5646,3601,1556,7705,9757,1572,9777,3635,7736,5692,9795,3656,7773,6758,7783,7792,9842,9847,1667,7813,8813,9873,1682,1683,9880,1648,9899,3756,1710,5811,3769,9916,7114,4725,1728,9924,5835,3790,4387,740,7906,5859,1778,3828,3830,1784,9983,1799,9994,5901,1807,1810,5909,8836,1818,5919,5921,1827,7978,5931,3900,1853,7998,3907,8005,8012,3925,8030,3935,3940,5989,8038,3730,5998,3953,8054,1914,6020,6023,1931,1934,6031,8080,1688,8516,1955,4006,4007,6059,6064,1981,4037,6087,1999,2002,4054,8159,4072,6124,2032,4083,2037,8186]))
print(datetime.now())


