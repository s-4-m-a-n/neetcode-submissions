class Solution:
    def findMaxConsecutiveOnes(self, nums: List[int]) -> int:
        max_one = 0
        seq_len = 0
        for i in nums:
            if i == 1:
                seq_len += 1
            else:
                if seq_len > max_one:
                    max_one = seq_len
                seq_len = 0
        if seq_len > max_one:
            max_one = seq_len
        return max_one