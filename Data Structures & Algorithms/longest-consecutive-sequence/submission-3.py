class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        nums = set(nums)
        longest_seq = 0
        for n in nums:
            if n-1 not in nums:
                length = 1
                while n+length in nums:
                    length += 1

                if length > longest_seq:
                    longest_seq = length
        return longest_seq