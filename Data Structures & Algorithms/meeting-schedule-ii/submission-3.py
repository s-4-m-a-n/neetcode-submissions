"""
Definition of Interval:
class Interval(object):
    def __init__(self, start, end):
        self.start = start
        self.end = end
"""

class Solution:
    def minMeetingRooms(self, intervals: List[Interval]) -> int:
        time = []
        for i in intervals:
            time.append((i.start, 1)) # 1 : meeting started
            time.append((i.end, -1)) # -1: meeting ended
        
        time.sort(key=lambda item: (item[0], item[1])) # sort by 0th item and if 0th values are equal then use the ended value i.e 1th 
        max_count, count = 0, 0
        for i in time:
            count += i[1] #either 0 or 1
            max_count = max(max_count, count)
        return max_count
