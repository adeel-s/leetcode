'''
===#134 Gas Station===
-Input
    List[int] gas: a list of the amount of gas at each gas station
        gas[i] is between 0 and 1000
    List[int] cost: the amount of gas it costs to get to the next station
        cost[i] is between 0 and 1000
    len(gas) == len(cost) == 1000

-Output
    int result: the starting index at which you can make a full circuit
        If there is one, there will only be one

-Observations
    * Each station also has an implicit excess gas value:
        gas[i] - cost[i] = the gas I'm left over with after reaching the next station
    * One solution:
        for each negative value, sum all the values before it:
            if that value is negative, I can't make a circuit from that value
            return the value for which I can
            or return -1 if I can never make a circuit
        This is O(n^2) time
    * I know if it's possible by summing the excess list
        if negative, a circuit isn't possible
    * I would only ever start at a positive excess index
    * Is it true that IF the sum of excess is positive, I want to start
        with the biggest excess?
        No. Excess list: 6, -7, 2, -1
            Start at 6, fail. Start at 2, win
    * Is there an inflection point? At which I know the array can't go negative?
    * This is the problem max subarray, on the excess array
    Proposal:
        create excess array
        (assume no wrap around)
        look for the max subarray in the excess array
            if the running sum every goes negative:
                restart
        If the sum of the excess array is greater thanzero, the starting index 
            is the start of the sub array.

        How to deal with a wrap-around subarray:
            Manually: split nums in half and then flip around the two halves
                run the algorithm again
-Solution
    result = -1
    excessSum = 0
    subarray = 0
    best = 0
    excess = [g + c for g, c in zip(gas, cost)]

    for i in range(len(excess)):
        excessSum += excess[i]
        if subarray + excess[i] < subarray:



    

'''
class Solution:
    def canCompleteCircuit(self, gas: List[int], cost: List[int]) -> int:
        if sum(gas) < sum(cost):
            return -1

        total = 0
        result = 0

        for i in range(len(gas)):
            total += gas[i] - cost[i]

            if total < 0:
                total = 0
                result = i + 1

        return result

                

             
        