class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        result = [0] * len(temperatures)
        stack = []
        for idx, temp in enumerate(temperatures):
            while stack and stack[-1][0] < temp:
                s_temp, s_idx = stack.pop()
                result[s_idx] = idx - s_idx
            stack.append((temp, idx))
        return result
