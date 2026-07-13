class Solution:
    def trap(self, height: List[int]) -> int:
        max_left = [0]
        max_right = [0]
        water_stored = []

        max_h = 0
        for i in range(1, len(height)):
            max_h = max(height[i-1], max_h)
            max_left.append(max_h)
        
        max_h = 0
        for i in range(1, len(height)):
            r_i = len(height)-1 - i
            max_h = max(height[r_i + 1], max_h)
            max_right.insert(0, max_h)
        
        for i in range(len(height)):
            w = min(max_left[i], max_right[i]) - height[i]
            water_stored.append(max(0, w))
        
        return sum(water_stored)

