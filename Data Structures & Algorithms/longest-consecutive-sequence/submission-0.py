class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        start_points = []
        nums = set(nums)
        for n in nums:
            if n-1 not in nums:
                start_points.append(n)
        max_seq_len = 0
        for s in start_points:
            c = 1
            while s+1 in nums:
                c +=1
                s += 1
            if c > max_seq_len:
                max_seq_len = c
        return max_seq_len
        
            
