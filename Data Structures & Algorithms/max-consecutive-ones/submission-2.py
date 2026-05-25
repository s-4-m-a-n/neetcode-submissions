class Solution:
    def findMaxConsecutiveOnes(self, nums: List[int]) -> int:
        max_len = 0
        seq_len = 0
        for n in nums:
            seq_len = seq_len + 1 if n else 0
            if seq_len > max_len:
                max_len = seq_len
        return max_len