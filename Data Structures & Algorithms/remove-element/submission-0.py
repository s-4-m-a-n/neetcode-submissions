class Solution:
    def removeElement(self, nums: list[int], val: int) -> int:
        lp = 0
        rp = 0
        while lp < len(nums):
            if nums[lp] == val:
                while nums[rp] == val:
                    rp += 1
                    if rp >= len(nums):
                        break
        
                if rp >= len(nums):
                    break
                
                temp = nums[lp]
                nums[lp] = nums[rp]
                nums[rp] = temp
            lp += 1
            rp = lp
        return lp
