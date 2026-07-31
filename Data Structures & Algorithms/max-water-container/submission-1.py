class Solution:
    def maxArea(self, heights: List[int]) -> int:
        l, r = 0, len(heights)-1
        max_qty = 0
        while l < r:
            qty = (r - l) * min(heights[l], heights[r])
            max_qty = max(max_qty, qty)

            if heights[l] < heights[r]:
                l += 1
            else:
                r -= 1

        return max_qty
