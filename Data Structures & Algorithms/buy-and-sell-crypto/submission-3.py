class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        max_profit = 0
        lowest = prices[0]

        for sell in prices:
            max_profit = max(sell - lowest, max_profit)
            lowest = min(sell, lowest)
        return max_profit