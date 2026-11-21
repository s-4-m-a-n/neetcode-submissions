class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        prefix_mul = [1]
        s = 1
        for n in nums:
            s *= n
            prefix_mul.append(s)
        
        s = 1
        prod_except = [1]*len(nums)
        for i in range(len(nums)-1, -1, -1):
            prod = prefix_mul[i]*s
            prod_except[i] = prod
            s *= nums[i]

        return prod_except
        
