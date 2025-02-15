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
    * I need to start at the first element and get to the last.
    * Unless every element in nums is a 1, at some point I will have a range of values
        I can move to.
        If I look at the list as a series of steps, each step made up of a range
            of values, I can just count the number of these steps.
        Ex. Input: nums = [2,4,1,1,1,1], Output: 2
            The first element is 2:
                My next step is the elements from index 1 to 2
                From indicies 1 and 2, elements 4 and 1, I can move anywhere
                    from indices 3, 4, or 5. This is my next step
            Solution: I need to take two steps
        Basically, from the last range of elements, define a new range of elements:
            ex. index 0 → indicies 1-2
        The number of ranges, or steps defined is the number of jumps required.

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
        