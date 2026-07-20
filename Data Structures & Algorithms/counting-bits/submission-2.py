class Solution:
    def countBits(self, n: int) -> List[int]:
        counts = [None] * (n+1)
        for j in range(n+1):
            s = 0
            i = j
            while i:
                if counts[i]:
                    s += counts[i]
                    break
                i = i & (i-1)
                s += 1
            counts[j] = s
        return counts