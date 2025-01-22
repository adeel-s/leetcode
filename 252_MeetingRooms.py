'''
===#252: Meeting Rooms===
-Input
    List[tuple] intervals: a list of intervals with start and end times
-Output
    bool result: whether the list of intervals could represent a schedule without conflicts
-Complexity
    O(n) time, space (assuming)

-Observations
    * Intervals can overlap at their bounds: 
        (0,8),(8,10) is not considered a conflict at 8
    * I can find the earliest start time and latest end time in O(n) time
    * If I sorted the intervals by the start times:
        An set of intervals would be conflict free if each end time did not 
            conflict with the next start time
-Solution
    Sort intervals by start time
    for all but the last interval:
        if end > nextStart:
            return False
    return True

'''
"""
Definition of Interval:
class Interval(object):
    def __init__(self, start, end):
        self.start = start
        self.end = end
"""

class Solution:
    def canAttendMeetings(self, intervals: List[Interval]) -> bool:
        intervals = sorted(intervals, key=lambda x: x.start)
        for i in range(len(intervals) - 1):
            if intervals[i].end > intervals[i + 1].start:
                return False
        return True

