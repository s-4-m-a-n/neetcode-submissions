class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        if len(s) == 0:
            return 0
        
        l, r = 0, 1
        seen = {s[l]}
        max_len = 1

        while r < len(s):
            if s[r] not in seen:
                seen.add(s[r])
                r +=1
            else:
                s_len = r - l
                max_len = max(max_len, s_len)
                seen.remove(s[l])
                l += 1
        
        s_len = r - l
        max_len = max(max_len, s_len)
        
        return max_len
