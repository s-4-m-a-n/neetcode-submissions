class Solution:
    def pivotIndex(self, nums: List[int]) -> int:
        postfix_sum = {i: 0 for i in range(len(nums))}
        s = 0
        for i in range(len(nums)-1, -1, -1):
            s += nums[i]
            postfix_sum[i] = s
        
        s = 0
        for i in range(len(nums)):
            s += nums[i]
            if s == postfix_sum[i]:
                return i
        return -1
