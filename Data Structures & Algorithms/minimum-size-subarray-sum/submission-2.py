class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:
        l, r = 0, 0
        min_len = sum(nums) + 1
        window_sum = 0
        while r < len(nums):
            window_sum += nums[r]
            if window_sum >= target:
                window_sum -= nums[l]
                window_sum -= nums[r]
                min_len = min(min_len, r-l+1)
                l += 1
            else:
                r += 1

        return 0 if min_len > sum(nums) else min_len
