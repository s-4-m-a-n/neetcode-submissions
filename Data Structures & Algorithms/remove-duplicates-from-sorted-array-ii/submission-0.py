class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        l = 2
        while l < len(nums):
            if nums[l-2] == nums[l]:
                nums.pop(l)
            else:
                l += 1
        return len(nums)