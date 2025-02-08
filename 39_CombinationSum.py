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
    * Combinations, not permutations
    * I think when DFS chooses a number, it shouldn't choose a lower number later
    * Proposal:
        Create an array for the result, and an array to backtrack with
        DFS:
            if the sum of all elements chosen is equal to the target:
                add to the result
            from i to the end of nums:
                add nums[i] to the backtracking list
                if sum of the backtracking list is less than or equal to the target
                    dfs
                remove nums[i] from the backtracking list


'''
class Solution:
    def combinationSum(self, nums: List[int], target: int) -> List[List[int]]:
        nums.sort()
        result = []
        choices = []
        comboSum = 0

        def DFS(i):
            if sum(choices) == target:
                result.append(choices.copy())
            for i in range(i, len(nums), 1):
                choices.append(nums[i])
                if sum(choices) <= target:
                    DFS(i)
                choices.pop()
        DFS(0)
        return result

        