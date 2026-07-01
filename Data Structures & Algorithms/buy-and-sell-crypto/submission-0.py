class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        max_profit = 0
        l, r = 0, 1
        
        while r < len(prices):
            profit = prices[r] - prices[l]
            if profit < 0:
                l = r
                r = l + 1
            else:
                r += 1
            
            max_profit = max(profit, max_profit)
        return max_profit
