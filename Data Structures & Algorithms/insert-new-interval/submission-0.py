class Solution:
    def insert(self, intervals: List[List[int]], new: List[int]) -> List[List[int]]:
        result = []

        processed = 0

        for start, end in intervals:
            if end < new[0]:
                result.append([start, end])
            elif start > new[1]:
                if processed == 0:
                    result.append(new)
                    processed = 1
                result.append([start, end])
            else:
                # overlap
                new[0] = min(start, new[0])
                new[1] = max(end, new[1])

        if processed == 0:
            result.append(new)

        return result