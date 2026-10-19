class Solution:
    def eraseOverlapIntervals(self, intervals: List[List[int]]) -> int:
        counts = 0
        intervals = sorted(intervals, key=lambda item: item[0])
        max_right_val = intervals[0][1]
        for i in range(1, len(intervals)):
            if intervals[i][0] < max_right_val: #overlapping
                max_right_val = min(max_right_val, intervals[i][1])
                counts += 1
            else:
                max_right_val = intervals[i][1]
        return counts

