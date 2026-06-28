import math

class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        l, r = 1, max(piles)
        min_m = r

        while l <= r:
            m = (l + r)//2
            taken_h = 0
            for p in piles:
                taken_h += math.ceil(p/m)

            if m < min_m and taken_h <= h:
                min_m = m

            if taken_h <= h:
                r = m - 1

            elif taken_h > h:
                l = m + 1

        return min_m