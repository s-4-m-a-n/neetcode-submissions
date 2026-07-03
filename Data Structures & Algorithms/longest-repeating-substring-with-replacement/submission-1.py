class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        l,r = 0, 0
        freq_table = {s[r]: 1}
        max_len = 0
        while r < len(s):
            c = s[r]
            sub_s_len = r - l + 1

            high_freq = -1
            for f in freq_table.values():
                high_freq = max(f, high_freq)

            print("r:", r, "l:", l, "len:", sub_s_len, "high_freq:", high_freq)
            if sub_s_len - high_freq <= k:
                print(sub_s_len - high_freq)
                max_len = max(max_len, sub_s_len)
                print(max_len)
                r += 1
                
                if r >= len(s):
                    break
                
                c = s[r]
                if not c in freq_table:
                    freq_table[c] = 1
                else:
                    freq_table[c] += 1
            else:
                freq_table[s[l]] -= 1
                l += 1
            print(freq_table)
        return max_len