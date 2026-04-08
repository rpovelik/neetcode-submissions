class Solution:
    def maxArea(self, heights: List[int]) -> int:
        l = 0
        r = len(heights) - 1
        volume = (r - l) * min(heights[l], heights[r])

        while l < r:
            if heights[l] < heights[r]:
                l += 1
            else:
                r -= 1

            volume = max((r - l) * min(heights[l], heights[r]), volume)

        return volume