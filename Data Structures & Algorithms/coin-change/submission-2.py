class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        dp = {}

        def dfs(rem_amt):
            if rem_amt == 0:
                return 0
            if rem_amt in dp:
                return dp[rem_amt]
            
            counts = amount + 1
            for coin in coins:
                if rem_amt - coin >= 0:
                    counts = min(counts, 1+dfs(rem_amt-coin))

            dp[rem_amt] = counts
            return counts

        min_counts = dfs(amount)
        return -1 if min_counts >= amount + 1 else min_counts
