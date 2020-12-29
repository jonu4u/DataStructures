# 253. Meeting Rooms II
#
# Given an array of meeting time intervals consisting of start and end times [[s1,e1],[s2,e2],...] (si < ei), find the minimum number of conference rooms required.
#
# Example 1:
#
# Input: [[0, 30],[5, 10],[15, 20]]
# Output: 2
# Example 2:
#
# Input: [[7,10],[2,4]]
# Output: 1
import heapq
from collections import defaultdict
class Solution(object):

    def minMeetingRooms(self, intervals):
        """
        :type intervals: List[List[int]]
        :rtype: int
        """
        # First we sort intervals based on start time
        intervals.sort(intervals,key=lambda item:item[0])

        # Take a hashmap to store the meeting rooms
        room_map=defaultdict(list)
        ctr=0
        len_val=len(intervals)
        index=0
        # We take each meeting slot and check whether this
        # slot can be placed in any meeting room. Just check the last meeting of the
        # meeting room to see if this can be placed as the list of meetings is sorted
        while index<len_val:
            start,end=intervals[index]
            index+=1
            is_found=False
            for key in room_map.keys():
                value_list=room_map[key]
                sz=len(value_list)
                # Since the start times are is sorted it is sufficient to take
                # the last value of each list as that is greatest
                last=value_list[sz-1]

                # We check whether the current element is on range of previous,
                # if yes then we continue as we need a new room.
                # So start between last or end between last
                if (start>=last[0] and start<last[1]) or (end<=last[1] and end>last[0]):
                        continue
                # When a room is found we break
                value_list.append([start,end])
                is_found=True
                break

            if not is_found:
                room_map[ctr].append([start,end])
                ctr+=1
        return len(room_map)


    # Doing this solution using Heap is Fast
    def minMeetingRooms_using_heap(self, intervals):

        # If there is no meeting to schedule then no room needs to be allocated.
        if not intervals:
            return 0

        # The heap initialization
        free_rooms = []

        # Sort the meetings in increasing order of their start time.
        intervals.sort(key= lambda x: x[0])

        # Add the first meeting. We have to give a new room to the first meeting.
        heapq.heappush(free_rooms, intervals[0][1])

        # For all the remaining meeting rooms
        for i in intervals[1:]:

            # If the room due to free up the earliest is free, assign that room to this meeting.
            if free_rooms[0] <= i[0]:
                heapq.heappop(free_rooms)

            # If a new room is to be assigned, then also we add to the heap,
            # If an old room is allocated, then also we have to add to the heap with updated end time.
            heapq.heappush(free_rooms, i[1])

        # The size of the heap tells us the minimum rooms required for all the meetings.
        return len(free_rooms)

s=Solution()
print(s.minMeetingRooms([[0, 30],[5, 10],[15, 20]]))
print(s.minMeetingRooms([[7,10],[2,4]]))
print(s.minMeetingRooms([[9,10],[4,9],[4,17]]))
print(s.minMeetingRooms([[6,10],[13,14],[12,14]]))
print(s.minMeetingRooms([[2,3],[8,9],[8,9]]))


