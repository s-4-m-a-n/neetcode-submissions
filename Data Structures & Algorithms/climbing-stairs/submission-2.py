class Solution:
    def climbStairs(self, n: int) -> int:
        lookup = [-1]*(n+1)
        for i in range(n, -1, -1):
            if i == n:
                lookup[i] = 1
            elif i == n-1:
                lookup[i] = 1
            else:
                lookup[i] = lookup[i+1] + lookup[i+2]
                
        return lookup[0]
            
