class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        differences = set()
        index_lookup = {}

        for i, n in enumerate(nums):
            diff = target - n

            if diff in differences:
                return [index_lookup[diff], i]
            
            differences.add(n)
            index_lookup[n] = i
        
