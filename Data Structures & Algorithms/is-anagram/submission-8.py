class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False
        
        counter = {}
        for s,d in zip(s, t):
            if s in counter:
                counter[s] += 1
            else:
                counter[s] = 1
            
            if d in counter:
                counter[d] -= 1
            else:
                counter[d] = -1
        
        for k, v in counter.items():
            if v != 0:
                return False
        return True