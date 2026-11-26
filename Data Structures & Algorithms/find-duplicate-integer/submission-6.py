class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
        slow, fast, slow_2 = 0, 0, 0
        while True:
            slow = nums[slow]
            fast = nums[nums[fast]]
            if slow == fast:
                break
        
        while slow != slow_2:
            slow = nums[slow]
            slow_2 = nums[slow_2]
        return slow

        
