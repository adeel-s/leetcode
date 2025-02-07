
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
    * For each element in the list:
        Perform Two sum II
        If i == i-1:
            skip the element
    * Proposal:
        nums = sorted nums
        result = []
        for i in range(len(nums) - 2):
            if nums[i] == nums[i+1]:
                continue
            lp = i + 1
            rp = len(nums) - 1
            while lp < rp:
                if nums[lp] + nums[rp] + nums[i] == 0:
                    result.append(nums[i], nums[lp], nums[rp])
                elif nums[lp] + nums[rp] + nums[i] > 0:
                    rp -= 1
                else:
                    lp += 1
        return result

'''
class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        result = []
        for i in range(len(nums) - 2):
            if nums[i] == nums[i-1] and i > 0:
                continue
            lp = i + 1
            rp = len(nums) - 1
            print(i, lp, rp)
            while lp < rp:
                if nums[lp] + nums[rp] + nums[i] == 0:
                    result.append([nums[i], nums[lp], nums[rp]])
                    lp += 1
                    while nums[lp] == nums[lp-1] and lp < rp:
                        lp += 1
                elif nums[lp] + nums[rp] + nums[i] > 0:
                    rp -= 1
                else:
                    lp += 1
        return result


        