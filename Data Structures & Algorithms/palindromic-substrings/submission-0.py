class Solution:
    def countSubstrings(self, s: str) -> int:
        if not s:
            return 0

        s = list(s)
        # odd palindrome
        counts = 0
        for i in range(len(s)):
            l, r = i, i
            while l >= 0 and r < len(s) and s[l] == s[r]:
                counts +=1
                l -= 1
                r += 1
            
        # even palindrome
        for i in range(len(s)):
            l = i
            r = l+1
            while l >= 0 and r < len(s) and s[l] == s[r]:
                counts +=1
                l -= 1
                r += 1 

        return counts