class Solution:
    def findMin(self, nums: List[int]) -> int:
        l, r = 0, len(nums)-1
        min_val = nums[0]

        while l <= r:
            if nums[l] <= nums[r]:
                min_val = min(nums[l], min_val)
                break

            m = (l + r) // 2
            min_val = min(nums[m], min_val)
            if nums[l] <= nums[m]:
                l = m + 1
            else:
                r = m - 1
        return min_val