class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        buy_price = float("inf")
        top = 0

        for price in prices:
            top = max(price - buy_price, top)
            buy_price = min(price, buy_price)
        
        return top