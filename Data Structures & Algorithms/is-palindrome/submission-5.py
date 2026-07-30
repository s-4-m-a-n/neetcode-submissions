class Solution:
    def isPalindrome(self, s: str) -> bool:
        l, r = 0, len(s)-1
        is_valid = True
        while l < r:
            l_c = s[l]
            r_c = s[r]

            if not l_c.isalpha() and not l_c.isdigit():
                l += 1
                continue
            
            if not r_c.isalpha() and not r_c.isdigit():
                r -= 1
                continue

            if l_c.lower() != r_c.lower():
                is_valid = False
                break

            l += 1
            r -= 1
            
        return is_valid