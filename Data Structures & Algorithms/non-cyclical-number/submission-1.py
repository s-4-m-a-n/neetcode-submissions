class Solution:
    def isHappy(self, n: int) -> bool:
        def sq_digit(n):
            digits = str(n)
            return sum([int(d)**2 for d in digits])
        
        seen = {n}
        is_happy = False
        
        while True:
            n = sq_digit(n)
            if n == 1:
                is_happy = True
                break
            elif n in seen:
                break
                
            seen.add(n)

        return is_happy