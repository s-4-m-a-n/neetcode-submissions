class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        s = nums[0]
        for n in nums[1:]:
            s = s ^ n
        return s