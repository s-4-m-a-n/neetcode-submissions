class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        from collections import defaultdict, Counter
        return(Counter(s) == Counter(t))