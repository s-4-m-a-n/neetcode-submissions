class Solution:
    def removeElement(self, nums: list[int], val: int) -> int:
        lp = 0
        rp = len(nums) -1
        while lp <= rp:
            if nums[lp] == val:
                temp = nums[lp]
                nums[lp] = nums[rp]
                nums[rp] = temp
                rp -= 1
            else:
                lp += 1
    
        return lp