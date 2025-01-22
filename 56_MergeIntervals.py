'''
===#56 Merge Intervals===
-Input
    List[List[int]] intervals: a list of intervals with start and end times
        intervals isn't sorted, and its intervals can be overlapping
-Output
    List[List[int]] result: a list of intervals without any overlapping intervals

-Complexity
    O(nlogn) time
    O(n) space

-Observations
    * Once sorted, overlapping intervals will always be adjacent
    * Adjacent intervals are overlapping if:
        interval[i].end > interval[i+1].start

-Solution:
    create a result list
    sort intervals by start time
    iterate through intervals:
        if intervals[i] conflicts with intervals[i+1]:
            merge into intervals[i+1]
        else:
            add to result list
    Add the last element to the result list
    return result list
'''
class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        if not intervals:
            return []
        result = []
        intervals = sorted(intervals, key=lambda x: x[0])
        for i in range(len(intervals) - 1):
            if intervals[i][1] >= intervals[i+1][0]:
                intervals[i+1][0] = min(intervals[i][0], intervals[i+1][0])
                intervals[i+1][1] = max(intervals[i][1], intervals[i+1][1])
            else:
                result.append(intervals[i])
        result.append(intervals[len(intervals) - 1])
        return result
        