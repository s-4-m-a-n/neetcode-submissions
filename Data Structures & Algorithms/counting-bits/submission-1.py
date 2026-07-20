class Solution:
    def countBits(self, n: int) -> List[int]:
        counts = []
        for i in range(n+1):
            s = 0
            while i:
                i = i & (i-1)
                s += 1
            counts.append(s)

        return counts