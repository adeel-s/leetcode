
'''
===Two Integer Sum II===

-Input
List[int] numbers: a list of integers in non-decreasing order
int target: a target which only two elements in .numbers add up to
-Output
List[int] result: the 1-indexed indices of the two numbers in 
    .numbers which add to .target
    
-Complexity
O(n) time
O(1) space

-Solution: check for compliments in a dictionary
Store each number and its index in a dictionary
for every number in .numbers, check for its compliment in the
    dictionary
return the indicies as described
*Problem: O(n) space

Solution: Two pointers
Initialize two points to the first and last indices of .numbers
If their sum is greater than .target, decrement the high pointer
If less than .target, increment the low pointer
Otherwise return the two indices

'''
class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        l, r = 0, len(numbers) - 1
        while l < r:
            if (numbers[l] + numbers[r]) > target:
                r -= 1
            elif (numbers[l] + numbers[r]) < target:
                l += 1
            else:
                return [l + 1, r + 1]
        return []
