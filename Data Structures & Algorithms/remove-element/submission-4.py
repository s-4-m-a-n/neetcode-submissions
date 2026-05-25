class Solution:
    def removeElement(self, nums: list[int], val: int) -> int:
        lp = 0
        rp = len(nums)
        while lp < rp:
            if nums[lp] == val:
                rp -= 1
                nums[lp] = nums[rp]
            else:
                lp += 1
    
        return lp