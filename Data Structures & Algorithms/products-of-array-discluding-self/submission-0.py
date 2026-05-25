class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        prefix_array = [1] * len(nums)
        postfix_array = [1] * len(nums)
        for i in range(1, len(nums)):
            prefix_array[i] = prefix_array[i-1] * nums[i-1]

        for j in range(len(nums)-2, -1, -1):
            postfix_array[j] = postfix_array[j+1] * nums[j+1] 
            prefix_array[j] *= postfix_array[j]

        return prefix_array
