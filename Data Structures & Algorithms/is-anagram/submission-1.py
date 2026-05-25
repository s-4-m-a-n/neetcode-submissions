class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False
        
        char_counts = {}
        unique_chars = set()
        for c in list(s):
            if c in char_counts:
                char_counts[c] += 1
            else:
                char_counts[c] = 1
                unique_chars.add(c)
                
        for c in list(t):
            if c not in unique_chars:
                return False
            char_counts[c] -= 1
            if char_counts[c] < 0:
                return False

        for k, v in char_counts.items():
            if v != 0:
                return False
        return True