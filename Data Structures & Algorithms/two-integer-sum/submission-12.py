class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        diffs = set()
        index_lookup = {}

        for i, n in enumerate(nums):
            diff = target - n

            if diff in diffs:
                return [index_lookup[diff], i]
            
            diffs.add(n)
            index_lookup[n] = i
        
        