'''
===#53 Maximum Subarray===

-Input
    List[int] nums: a list of integers
        nums[i] is between -1000 and 1000
        len(nums) is between 1 and 1000

-Output
    int result: the maximum sum of a sequence of contiguous numbers in nums

-Complexity
    N/A

-Observations
    * A list of one, nums[0 is the max]
    * The two pointers pattern sounds useful because the subarray is contiguous
    * Proposal:
        calculate the sum of the list
        lp and rp
        move whichever points to the lower value
        keep a running best on every move
    * While iterating through the array, if the running sum ever goes negative
        I can drop it and start over
        Do this and track the best
'''
class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        result = nums[0]
        best = 0

        for n in nums:
            if best < 0: 
                best = 0
            best += n
            result = max(result, best)

        return result
        