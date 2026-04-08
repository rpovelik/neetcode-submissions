class Solution:
    def maxArea(self, heights: List[int]) -> int:
        heights = sorted(enumerate(heights), key=lambda x: x[1], reverse=True)

        l = heights[0]
        r = heights[1]

        if l[0] > r[0]:
            l, r = r, l

        l_idx, r_idx = l[0], r[0]
        height = min(l[1], r[1])
        volume = (r_idx - l_idx) * height

        for h in heights[2:]:
            if h[0] > l_idx and h[0] < r_idx:
                continue
            elif h[0] < l_idx:
                l = h
                l_idx = l[0]
            else:
                r = h
                r_idx = r[0]
 
            height = min(l[1], r[1])
            volume = max((r_idx - l_idx) * height, volume)

        return volume