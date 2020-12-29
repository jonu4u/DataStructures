# 1705. Maximum Number of Eaten Apples
#
# There is a special kind of apple tree that grows apples every day for n days. On the ith day, the tree grows apples[i] apples that will rot after days[i] days, that is on day i + days[i] the apples will be rotten and cannot be eaten. On some days, the apple tree does not grow any apples, which are denoted by apples[i] == 0 and days[i] == 0.
#
# You decided to eat at most one apple a day (to keep the doctors away). Note that you can keep eating after the first n days.
#
# Given two integer arrays days and apples of length n, return the maximum number of apples you can eat.
#
#
#
# Example 1:
#
# Input: apples = [1,2,3,5,2], days = [3,2,1,4,2]
# Output: 7
# Explanation: You can eat 7 apples:
# - On the first day, you eat an apple that grew on the first day.
# - On the second day, you eat an apple that grew on the second day.
# - On the third day, you eat an apple that grew on the second day. After this day, the apples that grew on the third day rot.
# - On the fourth to the seventh days, you eat apples that grew on the fourth day.
# Example 2:
#
# Input: apples = [3,0,0,0,0,2], days = [3,0,0,0,0,2]
# Output: 5
# Explanation: You can eat 5 apples:
# - On the first to the third day you eat apples that grew on the first day.
# - Do nothing on the fouth and fifth days.
# - On the sixth and seventh days you eat apples that grew on the sixth day.
#
#
# Constraints:
#
# apples.length == n
# days.length == n
# 1 <= n <= 2 * 104
# 0 <= apples[i], days[i] <= 2 * 104
# days[i] = 0 if and only if apples[i] = 0.
class Solution(object):
    def eatenApples(self, apples, days):
        """
        :type apples: List[int]
        :type days: List[int]
        :rtype: int
        """
        day=0
        ctr=0
        sz=len(apples)
        for i in range(sz):
            apple=apples[i]
            rot_day=days[i]
            # If there are no apples we don't do anything in that day
            if apple==0:
                if ctr>day:
                    day+=1
                continue
            # If we're at a day where rot day less < current day those apples can't be used
            if (i+rot_day)<=day:
                if ctr>day:
                    day+=1
                continue
            ctr+=min(apple,rot_day)
            day+=min(apple,rot_day)
        return ctr

s=Solution()
s.eatenApples([9,24,5,12,15,21,13,12,28,0,21,6,0,26,20,0,21,21,7,0,19,25,0,30,32,32,0,0,0,22,0,11,2,27,16,0,15,12,14,33,10,11,0,13,11,0,27,0,0,14,20,11,0,22,10,1,22,6,0,13,31,33,30,27,2,30,18],
              [3,48,2,21,20,13,25,9,20,0,34,6,0,33,38,0,42,24,9,0,20,38,0,30,52,22,0,0,0,27,0,22,2,53,8,0,10,18,1,62,20,15,0,9,13,0,28,0,0,24,2,2,0,9,3,2,1,2,0,15,46,58,37,12,1,28,29])