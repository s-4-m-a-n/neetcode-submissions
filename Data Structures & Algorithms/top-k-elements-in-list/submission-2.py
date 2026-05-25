
class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        l_num = len(nums)
        freq_table = {}
        index_table = {}

        for n in nums:
            if n in index_table:
                index_table[n] += 1
            else:
                index_table[n] = 1
        
        for n, f in index_table.items():
            if f in freq_table:
                freq_table[f].append(n)
            else:
                freq_table[f] = [n]

        top_k_n = []
        for idx in range(l_num):
            if l_num-idx in freq_table:
                n = freq_table[l_num-idx]
                top_k_n.extend(n)
            if len(top_k_n) >= k:
                return top_k_n[:k]

        return top_k_n[:k]

