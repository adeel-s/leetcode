'''
===#198 House Robber===
-Input
    List[int] nums: a list of houses' values
-Output
    int result: the maximum value I can obtain as a robber
        from the houses without robbing consecutive houses
    
-Complexity
    O(n) time, space

-Observations
    * Feels like stair climbing - generally I want to rob as many
        houses as possible, but can't rob consequtive houses, so I
        want to skip 1 or 2 houses every time?
    * Track max value obtained at each house from all previous houses
    * Proposal:
        for each house:
            add its current value to the map value of houses i+2 and i+3
        The last two map values will be the best possible values
            return the max

-Solution
    #deal with edge cases of few nums
    values = [0] * len(nums)
    values[0] = nums[0]
    values[1] = nums[1]
    for i in range(len(nums) - 2):
        values[i+2] = max(values[i+2], values[i] + nums[i])
        if i < len(nums) - 2:
            values[i+3] = max(values[i+3], values[i] + nums[i])
    return max(values[len(values) - 1], values[len(values) - 2])

'''
class Solution:
    def rob(self, nums: List[int]) -> int:
        if len(nums) == 1:
            return nums[0]

        values = [0] * len(nums)
        values[0] = nums[0]
        values[1] = nums[1]

        for i in range(len(nums) - 2):
            values[i+2] = max(values[i+2], values[i] + nums[i+2])
            if i < len(nums) - 3:
                values[i+3] = max(values[i+3], values[i] + nums[i+3])

        return max(values[len(values) - 1], values[len(values) - 2])


        