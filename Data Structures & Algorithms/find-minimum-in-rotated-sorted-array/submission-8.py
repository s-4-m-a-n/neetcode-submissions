class Solution:
    def findMin(self, nums: List[int]) -> int:
        l, r = 0, len(nums)-1
        while l < r:
            p = (l + r) //2
            if nums[p] < nums[r]:
                r = p
            else:
                l = p+1
        return nums[l]