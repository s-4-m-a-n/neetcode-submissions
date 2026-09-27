class Solution:
    def rob(self, nums: List[int]) -> int:
        if len(nums) == 1:
            return nums[0]
            
        def rob_1(nums):
            r1, r2 = 0, 0
            for r in nums:
                t = max(r1+r, r2)
                r1 = r2
                r2 = t
            return r2
        
        return max(
                   rob_1(nums[1:]),
                   rob_1(nums[:-1]))