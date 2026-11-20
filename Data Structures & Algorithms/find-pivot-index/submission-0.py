class Solution:
    def pivotIndex(self, nums: List[int]) -> int:
        prefix_sum = []
        postfix_sum = []
        
        s = 0
        for i in range(len(nums)):
            s += nums[i]
            prefix_sum.append(s)

        s = 0
        for i in range(len(nums)-1, -1, -1):
            s += nums[i]
            postfix_sum.insert(0, s)

        for i in range(len(nums)):
            if prefix_sum[i] == postfix_sum[i]:
                return i
        return -1 