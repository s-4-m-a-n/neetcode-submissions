class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        result = []
        temp = None
        intervals.sort(key=lambda pair: pair[0])
        for interval in intervals:
            if not temp:
                temp = interval
                continue
            
            if temp[1] < interval[0]:
                result.append(temp)
                temp = interval
                continue
            
            elif temp[0] > interval[1]:
                result.append(interval)
            
            else:
                temp[0] = min(temp[0], interval[0])
                temp[1] = max(temp[1], interval[1])
            
        if temp:
            result.append(temp)
        return result