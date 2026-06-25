class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        max_area = 0
        stack = []
        for idx, h in enumerate(heights):
            if len(stack) == 0:
                stack.append((idx, h))

            elif h < stack[-1][1]:
                while stack and h < stack[-1][1]:
                    # pop the last item
                    prv_idx, prv_h = stack.pop()
                    area =  (idx - prv_idx) * prv_h
                    max_area = max(area, max_area)
                stack.append((prv_idx, h))
            else:
                stack.append((idx, h))

        end_idx = len(heights)
        while stack:
            idx, h = stack.pop()
            area = (end_idx - idx) * h
            max_area = max(area, max_area)
        return max_area