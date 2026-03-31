"""
Definition of Interval:
class Interval(object):
    def __init__(self, start, end):
        self.start = start
        self.end = end
"""
import heapq
class Solution:
    def minMeetingRooms(self, intervals: List[Interval]) -> int:
        if not intervals:
            return 0
        intervals.sort(key=lambda x:x.start)
        heap = []
        heapq.heappush(heap,intervals[0].end)
        rooms = 1
        for interval in intervals[1:]:
            if heap[0] > interval.start:
                heapq.heappush(heap, interval.end)
                rooms+=1
            else:
                heapq.heappop(heap)
                heapq.heappush(heap, interval.end)
        
        return rooms
