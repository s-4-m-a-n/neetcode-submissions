class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        result = [0]*len(temperatures)
        stack = []

        for i, t in enumerate(temperatures):
            while stack and stack[-1][0] < t:
                s_temp, s_idx = stack.pop()
                result[s_idx] = i - s_idx
            
            stack.append((t, i))
        return result