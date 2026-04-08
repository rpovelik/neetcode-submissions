class Solution:
    def eraseOverlapIntervals(self, intervals: List[List[int]]) -> int:
        intervals.sort(key=lambda x: x[1])
        c_start, c_end = intervals[0]
        removed = 0

        for start, end in intervals[1:]:
            if start < c_end:
                removed += 1
            else:
                c_start = start
                c_end = end

        return removed