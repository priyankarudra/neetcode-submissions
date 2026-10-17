"""
Definition of Interval:
class Interval(object):
    def __init__(self, start, end):
        self.start = start
        self.end = end
"""

class Solution:
    def minMeetingRooms(self, intervals: List[Interval]) -> int:
        length = len(intervals)

        meeting_start = sorted([i.start for i in intervals])
        meeting_end = sorted([i.end for i in intervals])

        rooms = count = 0
        index_start = index_end = 0        

        while index_start < length:
            if meeting_start[index_start] < meeting_end[index_end]:
                index_start += 1
                count += 1
            else:
                index_end += 1
                count -= 1
            rooms = max(rooms, count)

        return rooms

        


        
        