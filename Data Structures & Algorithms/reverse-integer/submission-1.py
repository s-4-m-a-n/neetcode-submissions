class Solution:
    def reverse(self, x: int) -> int:
        MIN = -2147483648  # -2^31,
        MAX = 2147483647  #  2^31 - 1
        
        x_str = str(x)
        if x_str[0] == "-":
            x = -int(x_str[1:][::-1])
        else:
            x = int(x_str[::-1])

        if x < MIN or x > MAX:
            return 0
        return x