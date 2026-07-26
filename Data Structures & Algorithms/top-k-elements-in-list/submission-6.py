from collections import defaultdict

class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        counts = defaultdict(int)
        for n in nums:
            counts[n] += 1
        
        freq_table = defaultdict(list)
        for n, f in counts.items():
            freq_table[f].append(n)
        
        k_most = []
        l_nums = len(nums)
        for idx in range(l_nums):
            if l_nums - idx in freq_table:
                k_most.extend(freq_table[l_nums-idx])
            
        return k_most[:k]