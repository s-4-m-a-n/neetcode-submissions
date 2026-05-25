class Solution:
    def isPalindrome(self, s: str) -> bool:
        l_pointer = 0
        r_pointer = len(s)-1
        while l_pointer < r_pointer:
            if not s[l_pointer].isalpha() and not s[l_pointer].isdigit():
                l_pointer += 1
                continue
            elif not s[r_pointer].isalpha() and not s[r_pointer].isdigit():
                r_pointer -= 1
                continue
            elif s[l_pointer].lower() != s[r_pointer].lower():
                return False
            l_pointer += 1
            r_pointer -= 1
        return True