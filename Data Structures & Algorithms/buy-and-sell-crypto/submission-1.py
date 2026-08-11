class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        l, r = 0, 1
        max_profit = 0

        while r<len(prices):
            profit = prices[r] - prices[l]
            if profit > 0:
                r = r + 1
            else:
                l = r
                r = r + 1
            max_profit = max(max_profit, profit)
        return max_profit