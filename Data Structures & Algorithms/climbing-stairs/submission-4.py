class Solution:
    def climbStairs(self, n: int) -> int:
        if n <= 2:
            # if n==1: 1 step 
            # if n==2: 1+1 or 2 so 2 steps in total
            return n

        lookup = [0] * (n+1)
        lookup[1] = 1
        lookup[2] = 2

        for i in range(3, n+1):
            lookup[i] = lookup[i-1] + lookup[i-2]
        return lookup[n]
