class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        l, r= 0, 0
        freq_table = {s[r]: 1}
        max_len = 0
        while r < len(s):
            c = s[r]
            high_freq = -1

            for f in freq_table.values():
                high_freq = max(high_freq, f)
            
            window_size = r-l+1

            if window_size - high_freq <= k:
                max_len  = max(max_len, window_size)
                r += 1
                if r >= len(s):
                    break
                
                c = s[r]
                if c in freq_table:
                    freq_table[c] += 1
                else:
                    freq_table[c] = 1
            else:
                c = s[l]
                freq_table[c] -= 1
                l += 1
        return max_len
            