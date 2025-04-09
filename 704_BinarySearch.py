'''
===704. Binary Search===

-Input
    int target: an integer to search for in the input list
        target is between -10000 and 10000
    List[int] nums: a list of integers to seach within
        nums is sorted and in ascending order
        len(nums) is between 1 and 10000
        nums[i] is between -10000 and 10000

-Output
    int result: the index of target in nums, or -1 if absent

-Complexity
    O(logn) time
    O(1) space

-Observations
    * This problem requires a simple binary search

-Solution
    low = 0
    high = len(nums) - 1
    mid = (low + high) / 2
    while (low <= high):
        if nums[mid] == target:
            return mid
        elif nums[mid] > target:
            high = mid - 1
            mid = (low + high) / 2
        else:
            low = mid + 1
            mid = (low + high) / 2
    return -1



        case 1: nums[mid] == target
            return target
        case 2: nums[mid] > target
            low = mid+1
        case 3: nums[mid] < target
            high = mid-1
'''
class Solution:
    def search(self, nums: List[int], target: int) -> int:

        low = 0
        high = len(nums) - 1
        mid = (low + high) // 2

        while (low <= high):

            if nums[mid] == target:
                return mid

            elif nums[mid] > target:
                high = mid - 1
                mid = (low + high) // 2

            else:
                low = mid + 1
                mid = (low + high) // 2

        return -1
        