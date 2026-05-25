class Solution:
    def search(self, nums: List[int], target: int) -> int:
        n = len(nums)
        if n == 0:
            return -1
        i = n // 2
        if nums[i] == target:
            return i
        elif nums[i] < target:
            r = self.search(nums[i+1:], target)
            return -1 if r==-1 else i+1+r
        else:
            return self.search(nums[:i], target)
