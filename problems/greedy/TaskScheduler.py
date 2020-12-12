# 621. Task Scheduler
#
# Given a characters array tasks, representing the tasks a CPU needs to do, where each letter represents a different task. Tasks could be done in any order. Each task is done in one unit of time. For each unit of time, the CPU could complete either one task or just be idle.
#
# However, there is a non-negative integer n that represents the cooldown period between two same tasks (the same letter in the array), that is that there must be at least n units of time between any two same tasks.
#
# Return the least number of units of times that the CPU will take to finish all the given tasks.
#
#
#
# Example 1:
#
# Input: tasks = ["A","A","A","B","B","B"], n = 2
# Output: 8
# Explanation:
# A -> B -> idle -> A -> B -> idle -> A -> B
# There is at least 2 units of time between any two same tasks.
# Example 2:
#
# Input: tasks = ["A","A","A","B","B","B"], n = 0
# Output: 6
# Explanation: On this case any permutation of size 6 would work since n = 0.
# ["A","A","A","B","B","B"]
# ["A","B","A","B","A","B"]
# ["B","B","B","A","A","A"]
# ...
# And so on.
# Example 3:
#
# Input: tasks = ["A","A","A","A","A","A","B","C","D","E","F","G"], n = 2
# Output: 16
# Explanation:
# One possible solution is
# A -> B -> C -> A -> D -> E -> A -> F -> G -> A -> idle -> idle -> A -> idle -> idle -> A
#
#
# Constraints:
#
# 1 <= task.length <= 104
# tasks[i] is upper-case English letter.
# The integer n is in the range [0, 100].
from collections import Counter
class Solution(object):
    def leastInterval(self, tasks, n):
        """
        :type tasks: List[str]
        :type n: int
        :rtype: int
        """
        ctr=0
        task_map=Counter(tasks)
        # WE SET A TIMER MAP
        cpu_counter_map={key:0 for key,val in sorted(task_map.items(),key=lambda item:item[1])}

        while True:
            min_key,min_val="",float('inf')
            for key,value in cpu_counter_map.items():
                if value<min_val:
                    min_val=value
                    min_key=key
            ctr+=1
            if ctr>=min_val:
                task_map[min_key]-=1
                if task_map[min_key]==0:
                    task_map.pop(min_key)
                    cpu_counter_map.pop(min_key)
                else:
                    cpu_counter_map[min_key]=ctr+n

            if not task_map:
                return ctr
s=Solution()
# print(s.leastInterval(["A","A","A","B","B","B"],2))
print(s.leastInterval(["A","A","A","A","A","A","B","C","D","E","F","G"], n = 2))
