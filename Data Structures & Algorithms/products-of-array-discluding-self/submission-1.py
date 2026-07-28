class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        fp = [1] * len(nums)
        bp = [1] * len(nums)
        result = [0] * len(nums)
        for i in range(1, len(nums)):
            fp[i] = fp[i-1] * nums[i-1]

        for i in range(len(nums)-2, -1, -1):
            bp[i] = bp[i+1] * nums[i+1]

        for i in range(len(nums)):
            result[i] = fp[i] * bp[i]

        return result
        
        

