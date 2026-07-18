class Solution:
    def myPow(self, x: float, n: int) -> float:
        p = 1
      
        for _ in range(abs(n)):
            p *= x

        if n < 0:
            p = 1/p
            
        return p