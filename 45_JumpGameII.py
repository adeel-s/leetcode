'''
===#45 Jump Game II===
-Input
    List[int] nums: a list of numbers representing how many spaces forward may be moved
    len(nums) is between 1 and 1000
    nums[i] is between 0 and 100
-Output
    int result: the minimum number of jumps to get to the last element in the list
        from the first. There will always be at least one path

-Observations
    * This also seems like a problem to approach backwards
'''
class Solution:
    def jump(self, nums: List[int]) -> int:
        result = 0
        lp = 0
        rp = 0
        while rp < len(nums) - 1:
            highest = 0
            for i in range(lp, rp + 1):
                highest = max(highest, i + nums[i])
            lp = rp + 1
            rp = highest
            result += 1
        return result
        