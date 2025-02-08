'''
===#40 Combination Sum II===
-Input
    List[int] candidates: a list of unsorted integers containing duplicates
        len(candidates) is between 1 and 100
        candidates[i] is between 1 and 50
    int target: an integer that elements in candidates will be summed to reach
        numbers from candidates may not be used more than once.
        target is between 1 and 30

-Output
    List[List[int]] result: a list of lists of numbers that sum to target
        result may not contain duplicates

-Complexity
    O(2^n * n) time
    O(n) space

-Observations
    * Backtracking
    * For each number, can I just choose to include it or not?
        No, because: candidates = [3,3,4], target = 7. 
        do/don't include the first 3, I end up with [3,4] and [3,4]
        This works if I store solutions in a set as tuples but isn't time optimal
    * I can sort for free
    * Proposal:
        For each element in candidates:
            if the sum of nums is equal to the target   
            add it to result and return
            add candidates[i] to nums
            if the sum of nums is less than or equal to the target
                recurse of i + 1
            pop from nums
            find the next element in nums that is not equal to nums[i]
            recurse on i + 1

'''
class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        candidates.sort()
        result = []
        combos = []


        def DFS(i):
            if target - sum(combos) == 0:
                result.append(combos.copy())
                return
            if target - sum(combos) < 0:
                return
            if i < len(candidates):
                combos.append(candidates[i])
                DFS(i + 1)
                combos.pop()
                i += 1
                while(i < len(candidates) and candidates[i] == candidates[i-1]):
                    i += 1
                DFS(i)

        DFS(0)
        return result


        