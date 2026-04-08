class Solution:
    def maxArea(self, heights: List[int]) -> int:
        answer = 0
        heights = sorted(enumerate(heights), key=lambda x: x[1], reverse=True)

        first = heights[0]
        second = heights[1]

        if first[0] > second[0]:
            first, second = second, first
        
        s, e = first[0], second[0]
        vol = min(first[1], second[1])
        answer = max((e - s) * vol, answer)

        for h in heights[2:]:
            if h[0] > s and h[0] < e:
                continue
            elif h[0] < s:
                first = h
                s = first[0]
            else:
                second = h
                e = second[0]

            vol = min(first[1], second[1])
            answer = max((e - s) * vol, answer)

        return answer