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
        def helper (houses: List[int]) -> int:
            first = 0
            second = 0

            for h in houses:
                current = max(h + first, second)
                first = second
                second = current
            
            return second

        return max(helper(nums[1:]), helper(nums[:-1]))
        
        