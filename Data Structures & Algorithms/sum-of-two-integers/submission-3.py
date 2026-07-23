class Solution:
    def getSum(self, a: int, b: int) -> int:
        MASK = 0xFFFFFFFF
        MAX_INT = 0x7FFFFFFF
        
        while b:
            a_xor_b = a ^ b
            a_and_b = (a & b) << 1 
            a = a_xor_b & MASK
            b = a_and_b & MASK
        return a if a <= MAX_INT else ~(a ^ MASK)