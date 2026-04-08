class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        intervals.sort(key=lambda x: x[0])

        result = []
        c_start, c_end = intervals[0]

        for start, end in intervals:
            if start <= c_end:
                c_end = max(end, c_end)
            else:
                result.append([c_start, c_end])
                c_start = start
                c_end = end

        result.append([c_start, c_end])

        return result