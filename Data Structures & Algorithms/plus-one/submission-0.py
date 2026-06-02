class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        large_int = 0
        for idx in range(len(digits)):
            large_int += 10**idx * digits[len(digits)-1-idx]
        large_int += 1
        large_inc_list = []
        prv_num = 0
        for i in range(len(str(large_int))-1, -1, -1):
            digit = large_int//10**i
            large_inc_list.append(digit-prv_num)
            prv_num = 10 * digit
        return large_inc_list