'''
===#39 Combination Sum===
-Input
    List[int] nums: a list of distinct integers
        len(nums) is between 1 and 20
        nums[i] is between 2 and 30
    int target: a target to sum numbers in nums to
        target is between 2 and 30
-Output
    List[List[int]] result: the list of all distinct sets of numbers
        in nums that sum to target

-Complexity
    O(2^(t/m)) time
    O(t/m) space
    where t is the target and m is the min value in nums

-Observations
    * Backtracking, based on time complexity
    * I think when DFS chooses a number, it shouldn't choose a lower number later

'''
class Solution:
    def combinationSum(self, nums: List[int], target: int) -> List[List[int]]:
        result = []
        choices = []
        comboSum = 0

        def DFS(i):
            if sum(choices) == target:
                result.append(choices)
            for n in nums[i:]:
                choices.append(n)
                if sum(choices) < target:
                    DFS(i + 1)
                choices.pop()
        DFS(0)
        return result

        