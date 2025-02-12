'''
===#55 Jump Game===
-Input
    List[int] nums: a list of numbers representing the number of forward
        steps that can be taken
        len(nums) is between 1 and 1000
        nums[i] is between 0 and 1000
-Output
    bool result: whether the last element can be reached from index 0

-Observations
    * If all previous elements lead to a 1 which is followed by a 0,
        the answer is False
    * 0 is never chosen as an option
    * Proposal: DP
        Store a bool value for each element representing whether it can be reached
        For each element:
            if it can be reached, update the elements it can reach.
    * Proposal: Greedy
        For each element, backwards:
            if that element is reachable, continue.
        if the first element is reached, return true


'''
class Solution:
    def canJump(self, nums: List[int]) -> bool:
        jump = 1
        for i in range(len(nums) - 2, -1 , -1):
            if nums[i] >= jump:
                jump = 1
                continue
            else:
                jump += 1

        return jump == 1

