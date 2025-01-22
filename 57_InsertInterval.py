'''
===#57 Insert Interval===
-Input
    List[List[int]] intervals: a list of non-overlapping intervals with start and end times
    List[int] newInterval: an interval to insert into intervals
-Output
    List[List[int]]: the updated list of intervals

-Complexity
    O(n) time, space

-Observations
    * I am interested in the end-time nearest to the start time of newInterval
        and the start time nearest to the end-time of newInterval
    * Intervals with end times less than newInterval's start time can be added
        to the result list
        Same with intervals whose start time is greater than newInterval's end time
    

-Solution
    While looping through the list:
    * Case 1: newInterval comes before current interval
        append newInterval, then the rest of the list, then return the resulting list
    * Case 2: current interval comes before newInterval:
        append current interval
    * Remaining cases: there is some overlap between current interval and newInterval
        Expand newInterval to absorb current interval - expand its bounds as needed

        
    initialize result list
    for i in range len(intervals):
        if newInterval.end is before intervals[i].start:
            add newIterval to the result, append the rest of the intervals and return
        else if newInterval.start is after intervals[i].end:
            add intervals[i] to result list
        else:
            absorb intervals[i] into newInterval

    add newInterval to result list
    return result list

        
        

'''
class Solution:
    def insert(self, intervals: List[List[int]], newInterval: List[int]) -> List[List[int]]:

        result = []

        for i in range(len(intervals)):
            # newInterval comes before the current interval:
                # add it to result and return the rest of the intervals
            if newInterval[1] < intervals[i][0]:
                result.append(newInterval)
                return result + intervals[i:]
            # newInterval comes after the current interval:
                # add the current interval to the result
            elif newInterval[0] > intervals[i][1]:
                result.append(intervals[i])
            # newInterval overlaps with the current interval
                # update the start and end of newInterval
            else:
                newInterval = [min(newInterval[0], intervals[i][0]), max(newInterval[1], intervals[i][1])]
            
        result.append(newInterval)
        return result
        