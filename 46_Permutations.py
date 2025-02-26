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
    * Proposal:
        Base case: nums is empty:
        permute for every element in nums, recursively
            return an empty list
        Otherwise:
            Insert nums[0] at every index in every permutation in the result list

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
        