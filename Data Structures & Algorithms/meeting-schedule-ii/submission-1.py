"""
Definition of Interval:
class Interval(object):
    def __init__(self, start, end):
        self.start = start
        self.end = end
"""

class Solution:
    def minMeetingRooms(self, intervals: List[Interval]) -> int:
        count = 0
        max_count = 0
        starts = sorted([item.start for item in intervals])
        ends = sorted([item.end for item in intervals])
        start_idx = 0
        end_idx = 0
        while True:
            if start_idx >= len(starts):
                return max_count

            if starts[start_idx] < ends[end_idx]:
                count += 1
                max_count = max(max_count, count)
                start_idx += 1
            else:
                count -= 1
                end_idx += 1

        return max_count