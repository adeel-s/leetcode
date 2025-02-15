'''
===#46 Permutations===
-Input
    List[int] nums: a list of numbers
        len(nums) is between 1 and 6
        nums[i] is between -10 and 10
-Output
    List[List[int]] result: the list of all possible permutations of 
        the elements in nums
-Complexity
    O(n*n!) time
    O(n) space

-Observations
    * Seems like backtracking but with permutations - so duplicates are fine.
    * dfs(i) → until i == len(nums)
    Proposal:
    backtrack:
        if len(nums) == 1:
            return nums[0]
        For each number in nums:
            perm.append(backtrack([1:-1]))

'''
class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        if len(nums) == 0:
            return [[]]
        perms = self.permute(nums[1:])
        result = []

        for p in perms:
            for i in range(len(p) + 1):
                pCopy = p.copy()
                pCopy.insert(i, nums[0])
                result.append(pCopy)
        return result
        