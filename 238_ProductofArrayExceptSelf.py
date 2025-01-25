
'''
===Product of Array Except Self===
-Input
int[] nums: an array of numbers
-Output
int[] result: an array of numbers, each element of which
    is the product of all the elements in .nums except the
    one at its corresponding index
-Complexity
Time: O(n)
Space: O(n)
-Solution without division:
first pass through .nums: load result elements with the 
    products of all previous elements
second pass through .nums: mulitple result pre-product values
    by post-product values
'''
class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        result = [1] * len(nums)
        pre, post = 1, 1
        for i in range(len(nums)):
            result[i] = pre
            pre *= nums[i]
        for i in range(len(nums) - 1, -1, -1):
            result[i] *= post
            post *= nums[i]
        return result
        
