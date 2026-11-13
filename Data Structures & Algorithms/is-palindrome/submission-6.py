class Solution:
    def isPalindrome(self, s: str) -> bool:
        l, r = 0, len(s)-1 
        is_valid = True
        while l < r:
            l_char = s[l].lower()
            r_char = s[r].lower()
            if not (l_char.isalpha() or l_char.isdigit()):
                l += 1
                continue
            
            if not (r_char.isalpha() or r_char.isdigit()):
                r -= 1
                continue
            
            if r_char != l_char:
                is_valid = False
                break
            l += 1
            r -= 1
        
        return is_valid
