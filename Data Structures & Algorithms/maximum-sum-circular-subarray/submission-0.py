class Solution:
    def maxSubarraySumCircular(self, nums: List[int]) -> int:
        curr_max = 0
        curr_min = 0
        global_max = nums[0]
        global_min = nums[0]
        total = 0
        for n in nums:
            total += n
            curr_max = max(curr_max+n, n)
            global_max = max(global_max, curr_max)
            
            curr_min = min(curr_min+n, n)
            global_min = min(global_min, curr_min)
        
        return global_max if global_max < 0 else max(total-global_min, global_max)
