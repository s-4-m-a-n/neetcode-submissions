class Solution:
    def climbStairs(self, n: int) -> int:
        lookup = [-1]*(n+1)
        def dfs(i):
            if i == n:
                return 1
            elif i > n:
                return 0
            if lookup[i] != -1:
                return lookup[i]
            lookup[i] = dfs(i+1) + dfs(i+2)
            return lookup[i]
        return dfs(0)
