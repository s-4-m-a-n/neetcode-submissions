from collections import defaultdict
class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        memory = defaultdict(int)
        max_len = 0

        for n in nums:
            if memory[n]:
                continue        
            memory[n] = memory[n-1] + memory[n+1] + 1
            memory[n - memory[n-1]] = memory[n]
            memory[n + memory[n+1]] = memory[n]    
            max_len = max(max_len, memory[n])
        return max_len


