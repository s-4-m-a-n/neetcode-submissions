from collections import defaultdict
class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        counters = defaultdict(int)
        if len(s) != len(t):
            return False

        for i, j in zip(s, t):
            counters[i] += 1
            counters[j] -= 1
        
        for k, v in counters.items():
            if v != 0:
                return False
        return True 
