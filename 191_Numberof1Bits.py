'''
===#191 Number of 1 bits===
-Input
    int n: a 32-bit interger
-Output
    int result: the number of 1 bits in n

-Observations:
    * If I count down from 32 and keep checking/subtracting from n,
        I can count the number of times I can subtract that power of 2
        from n. Increase result by one each time.
    * I can also AND/mod the bits and keep shifting them
'''
class Solution:
    def hammingWeight(self, n: int) -> int:
        result = 0
        while n:
            result += n % 2
            n = n >> 1
        return result