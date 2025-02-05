
'''
===#15 3Sum===
-Input
    List[int] nums: a list of integers
        len(nums) is between 3 and 1000
        nums[i] is between +/-100,000
-Output
    List[List[int]] result: all possible sets of unique triplets that add to 0

-Complexity
    O(n^2) time
    O(1) space (not including the result array, I assume)

-Observations
    * Sort the list
    * Have three pointers:
        One left
        One right
        One center
    * Based on the left and right, the center searches for the compliment to make a valid triplet
    * In the case of doubles, the center pointer will find a double if needed.
        * Left and right pointers should skip doubles if found
    * Proposal:
        Sort the list
        Initialize three pointers: lp, rp, cp to the start, end of the list
        Binary search for the compliment
        If found, add to the result list


'''
from typing import List


class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums = sorted(nums)
        print(nums)
        lp, rp = 0, len(nums) - 1
        result = []

        while lp < rp:
            low = lp + 1
            high = rp - 1
            while low <= high:
                mid = (high + low) // 2
                if nums[lp] + nums[rp] + nums[mid] == 0:
                    result.append([lp, mid, rp])
                elif nums[lp] + nums[rp] + nums[mid] < 0:
                    low = mid + 1
                else:
                    high = mid - 1
            if nums[lp] + nums[rp] + nums[high] > 0:
                i = 0
                while nums[rp-i] == nums[rp]:
                    rp -= 1
                    i -=1
            else:
                i = 0
                while nums[lp+i] == nums[lp]:
                    lp += 1
                    i +=1

        return result


        