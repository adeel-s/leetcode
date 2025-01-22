'''
===#253: Meeting Rooms 2===
-Input
    List[Interval] intervals: a list of intervals, each with a start and end time
-Output
    int result: the number of days it would take to schedule all meetings

-Complexity
    O(nlogn) time
    O(n) space

-Observations
    * Sorting sounds like a good idea again
    * The number of days is the maximum number of overlapping meetings
    * Track meetings starting and meetings ending:
        The number of days is equal to the maximum number of meetings started but not ended

-Solution
    Create sorted list of meeting start times
    Create sorted list of meeting end times

    for the length of the start array:
        if the next meeting is starting before a previous meeting has ended:
            move start pointer to next meeting
            increase number of concurrent meetings
        else:
            move end pointer to next meeting
            decrease number of concurrent meetings

        update max number of concurrent meetings
    return max number of concurrent meetings
    
'''
"""
Definition of Interval:
class Interval(object):
    def __init__(self, start, end):
        self.start = start
        self.end = end
"""

class Solution:
    def minMeetingRooms(self, intervals: List[Interval]) -> int:
        starts = sorted([i.start for i in intervals])
        ends = sorted([i.end for i in intervals])

        start, end = 0, 0

        result, concurrent = 0, 0

        while start < len(starts):
            if starts[start] < ends[end]:
                concurrent += 1
                start += 1
            else:
                concurrent -= 1
                end += 1
            result = max(result, concurrent)

        return result


        


        