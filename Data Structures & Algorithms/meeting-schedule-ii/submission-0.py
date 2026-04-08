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
        heap = []
        rooms = 0
        answer = rooms

        for interval in intervals:
            start, end = interval.start, interval.end
            heapq.heappush(heap, (start, 1))
            heapq.heappush(heap, (end, -1))
        
        while heap:
            dot = heapq.heappop(heap)
            rooms += dot[1]
            answer = max(answer, rooms)

        return answer