class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        start = 0
        end = len(prices)
        max_profit = 0
        profit = 0
        lowest = prices[start]

        while start < end:
            if prices[start] < lowest:
                lowest = prices[start]
            else:
                profit = prices[start] - lowest
                max_profit = max(profit, max_profit)
            start += 1 

        return max_profit