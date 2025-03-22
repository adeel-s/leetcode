'''
===152 Maximum Product Subarray===

-Input
    List[int] nums: a list of integers
        len(nums) is between 1 and 1000
        nums[i] is between -10 and 10

-Output
    int result: the product of the subarray
        result will always fit in a 32-bit integer

-Complexity
    O(n) time
    O(1) space

-Observations
    * Multiply all of the elements together, then divide strategically
        Not exactly because order matters: subarrays
    * Keep a running product
    * Is it true that result will always be either the entire array
        or pivot about one negative number?
        Yes
        Which negative number?
            The one with the smallest product preceeding it
                Absolute value?
        It will always be either the first or last negative number.

    * Proposal:
        Multiply all elements together
        if positive, return this
        else:
            find the first and last negative numbers
            divide the product by each
            return the max

    * Proposal:
        Keep track of min and max subarray products
            update according to the next element
            return max at the end

'''

class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        maxProd = 1
        minProd = 1
        result = max(nums)
        for n in nums:
            tempMax = maxProd
            maxProd = max(maxProd * n, minProd * n, n)
            minProd = min(minProd * n, tempMax * n, n)
            result = max(result, maxProd)
        return result