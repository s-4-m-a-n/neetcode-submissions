class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        l = 1
        while l < len(nums):
            if nums[l] == nums[l-1]:
                nums.remove(nums[l])
            else:
                l += 1
                
        return l