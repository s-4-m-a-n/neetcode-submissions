class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        res = max(nums)
        curr_min, curr_max = 1, 1

        for n in nums:
            temp = curr_max * n
            curr_max = max(curr_max * n, curr_min * n, n)
            curr_min = min(temp, curr_min * n, n)
            res = max(curr_max, res)
            
        return res





        
