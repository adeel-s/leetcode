'''
===#78 Subets===

-Input
    List[int] nums: a list of integers
        len(nums) is between 1 and 10
        nums[i] is between -10 and 10
-Output
    List[List[int]] result: all possible subsets of the
        elements of nums

-Complexity:
    O(n*2^n) time
    O(n) space

-Observations
    * Sounds like backtracking (O(2^n))
    * Kind of a DFS
    * Base case:
        i = len(nums) - 1
            add the subset to the result
    * Case 1:
        Add the next element of nums to the subset
        Run DFS
    * Case 2:
        Don't add the next element of nums to the subset
        Run DFS

-Solution:
    Run a DFS:
        In each recursion:
            if i is greater than the max index:
                Vase case: add a copy of the subset to the result
            Then:
            add nums[i] to the subset and recurse on the next element
            remove nums[i] from the subset and recurse on the next element
            

'''
class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        result = []
        subset = []
        def dfs(i):
            if i > len(nums) - 1:
                result.append(subset.copy())
                return
            subset.append(nums[i])
            dfs(i + 1)
            
            subset.pop()
            dfs(i + 1)
        dfs(0)
        return result



        