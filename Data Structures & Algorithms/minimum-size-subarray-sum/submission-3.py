class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:
        l, r = 0, 0
        min_len = float("inf")
        window_sum = 0
        for r in range(len(nums)):
            window_sum += nums[r]
            while window_sum >= target:
                window_sum -= nums[l]
                min_len = min(min_len, r-l+1)
                l += 1
        return 0 if min_len == float("inf") else min_len
