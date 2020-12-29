# 986. Interval List Intersections
#
# Given two lists of closed intervals, each list of intervals is pairwise disjoint and in sorted order.
#
# Return the intersection of these two interval lists.
#
# (Formally, a closed interval [a, b] (with a <= b) denotes the set of real numbers x with a <= x <= b.  The intersection of two closed intervals is a set of real numbers that is either empty, or can be represented as a closed interval.  For example, the intersection of [1, 3] and [2, 4] is [2, 3].)
#
# Example 1:
# Input: A = [[0,2],[5,10],[13,23],[24,25]], B = [[1,5],[8,12],[15,24],[25,26]]
# Output: [[1,2],[5,5],[8,10],[15,23],[24,24],[25,25]]
#
# Note:
# 0 <= A.length < 1000
# 0 <= B.length < 1000
# 0 <= A[i].start, A[i].end, B[i].start, B[i].end < 10^9
class Solution(object):
    def intervalIntersection(self, A, B):
        """
        :type A: List[List[int]]
        :type B: List[List[int]]
        :rtype: List[List[int]]
        """
        szA=len(A)
        szB=len(B)
        # We take two pointers in two lists, so that whenever the elements are within the rangeof each other we get an intersection
        l1,l2=0,0
        out=[]
        while l1<szA and l2<szB:
            # This is case when there is no intersection so begining of 1st element is > ending of second, so we increase te pointer of second list
            if A[l1][0]>B[l2][1]:
                l2+=1
                continue
            if B[l2][0]>A[l1][1]:
                l1+=1
                continue
            out.append(self.find_intersection(A[l1],B[l2]))
            # If the ending range of one element is more than the other we move to the next elemnt of the other list to see if there is an intersection
            # of the current wth the next element
            if A[l1][1]>B[l2][1]:
                l2+=1
            elif B[l2][1]>A[l1][1]:
                l1+=1
            else:
                l1+=1
                l2+=1
        return out
    def find_intersection(self,elem1,elem2):
        list=sorted(elem1+elem2)
        return list[1:len(list)-1]

s=Solution()
print(s.intervalIntersection(A = [[0,2],[5,10],[13,23],[24,25]], B = [[1,5],[8,12],[15,24],[25,26]]))
print(s.intervalIntersection(A = [[0,2],[5,10]], B = [[1,5]]))
print(s.intervalIntersection(A = [[0,2],[5,10]], B = [[1,5],[8,13],[15,23]]))
print(s.intervalIntersection(A = [[3,4]], B = [[1,2]]))
