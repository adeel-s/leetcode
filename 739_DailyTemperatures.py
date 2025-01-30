'''
===#739 Daily Temperatures===
-Input 
    List[int] temperatures: a list of daily temperatures
        len(temperatures) is between 1 and 1000
        temperatures[i] is between 1 and 100
-Output
    List[int] result: a list of numbers that represents a number of days
        after temperature[i] that a warmer day occurs
            Example: temperatures = [30, 38]
                result = [1, 0]
                a higher temperature than temperatures[0] occurs one day after it
                a higher temperature than temperatures[1] never occurs

-Complexity
    O(n) time, space

-Observations
    * The last value of result is always 0
    * A brute force solution would just look at every day after
        every other day for a higher temp
            This is O(n^2)
    * Monotonic decreasing (actually, non-increasing) order:
        Every time I see an element in temperatures larger than the top of the stack:
            pop everything smaller than it.
        In this case, add the difference in indices to the result array
    * Proposal:
        result = [0] * len(temp)
        add temp[0], 0 to the stack
        For every element after temp[0]:
        j = 1
            while temp[i] is greater than stack[i-j]:
                result[index of stack[i-j]] = i - index of stack[i-j]
                temp.pop()
                j += 1
            else:
                stack.push(temp[i])


                
'''
class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        result = [0] * len(temperatures)
        stack = []
        for i, t in enumerate(temperatures):
            while stack and t > stack[-1][1]:
                index, temp = stack.pop()
                result[index] = i - index
            stack.append((i, t))

        return result
        