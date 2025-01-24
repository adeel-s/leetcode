'''
===#1 Two Sum===

-Input
    List[int] nums: a list of numbers
        len(nums) is between 2 and 1000
        nums[i] is between +-10,000,000
    int target: the sum two numbers in nums must add to
        target is between +-10,000,000
-Output
    List[int] result: the two indices whose elements sum to target

-Complexity
    O(n) time, space

-Observations
    * Store each number in a dictionary along with its index
        for each number in nums, look for it's compliment
            a number's compliment is the difference of target and that number
        Only one solution exists, so the target will always be found

-Solution
    comps = {}
    for i in range(len(nums)):
        if comps.get(target - nums[i]):
            return [comps.get(target - nums[i]), i]
        else:
            comps.update({nums[i] : i})

'''
class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:

        comps = {}
        for i in range(len(nums)):
            if comps.get(target - nums[i]) != None:
                return [comps.get(target - nums[i]), i]
            else:
                comps.update({nums[i] : i})


        