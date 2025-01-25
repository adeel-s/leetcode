'''
===#213 House Robber II===
-Input
    List[int] nums: a list of values of houses
    len(nums) is between 1 and 100
    nums[i] is between 0 and 100
-Output
    int result: the maximum value I can extract from the houses
        without robbing consequtive houses, where the first
        and last houses are next to each other

-Complexity
    O(n) time, space

-Observations
    * If I take rob the first house, I must not rob the last
    * If I rob the last house, I must not rob the first
        * Just run the same algorithm twice: skip the first element, skip the last

'''
class Solution:
    def rob(self, nums: List[int]) -> int:
        if len(nums) == 1:
            return nums[0]
        def helper(houses: List[int]) -> int:
            if len(houses) == 1:
                return houses[0]
            values = [0] * len(houses)
            values[0] = houses[0]
            values[1] = houses[1]

            for i in range(len(houses) - 2):
                values[i+2] = max(values[i+2], values[i] + houses[i+2])
                if i < len(houses) - 3:
                    values[i+3] = max(values[i+3], values[i] + houses[i+3])
            return max(values[len(values) - 1], values[len(values) - 2])

        print(helper(nums[1:]), helper(nums[:-1]))
        return max(helper(nums[1:]), helper(nums[:-1]))
        
        