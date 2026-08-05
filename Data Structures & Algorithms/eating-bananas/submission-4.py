import math

class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        l, r= 1, max(piles)
        min_rate = r
        while l <= r:
            current_rate = (l + r)//2
            t = sum([math.ceil(p/current_rate) for p in piles])

            if t <= h:
                min_rate = min(min_rate, current_rate)
                r = current_rate-1
            else:
                l = current_rate + 1
        return min_rate