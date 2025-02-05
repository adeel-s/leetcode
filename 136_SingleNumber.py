'''
===#136 Single Number===

-Input
    List[int] nums: a list of numbers
        len(nums) is between 1 and 10000
        nums[i] is between +/-10000
-Output
    int result: the only number in the list that appears once - all others appear twice

-Complexity
    O(n) time
    O(1) space

-Observations:
    * Bitwise XOR operations are commutative:
        * a number XORed by itself = 0
        * Since all numbers appear twice in the list except one, only this number will remain
            if all elements are XORed together
'''
class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        result = 0
        for n in nums:
            result ^= n

        return result
