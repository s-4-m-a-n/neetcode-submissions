class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        char_counts = {}
        for c in list(s):
            if c in char_counts:
                char_counts[c] += 1
            else:
                char_counts[c] = 1
        
        for c in list(t):
            if c not in char_counts:
                return False
            char_counts[c] -= 1
            if char_counts[c] < 0:
                return False
        for k, v in char_counts.items():
            if v != 0:
                return False
        return True