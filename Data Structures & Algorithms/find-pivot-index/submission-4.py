# class Solution:
#     def pivotIndex(self, nums: List[int]) -> int:
#         total = sum(nums)
#         s = 0
#         for i in range(len(nums)):
#             s += nums[i]
#             if s == (total + nums[i] - s):
#                 return i
#         return -1

class Solution:
    def pivotIndex(self, nums: List[int]) -> int:
        total = sum(nums)
        s = 0
        for i in range(len(nums)):
            if s == (total - nums[i] - s):
                return i
            s += nums[i]
            
        return -1