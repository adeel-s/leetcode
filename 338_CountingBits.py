'''
===#338 Counting Bits===
-Input
    int n: the right bound of a range of numbers
        n is between 0 and 1000
-Output
    List[int] a list of the number of 1 bits required to produce the 
        the value of the index

-Observations
    * bits[i+1] = bits[i] -1/+0/+1, or 1. Always
    * How can I know whether it will go up, down, stay the same, or drop to 1?
    * The pattern of bits keeps repeating... 
    * Proposal: 
        Every time I hit a new power of 2, reset a pointer back to element 1
        Every successive element will be the number of bits at bits[pointer] + 1
    * How can I determine if I'm at a new power of 2?
        * Yes! n & (n - 1)

-Solution:
    initialize result array to all zeros, plus an extra zero as the base case
    initialize a pointer
    from 1 to n:
        if i is not a power of 2:
            result[i] = 1 + result[pointer]
        else:
            result[i] = 1

'''
class Solution:
    def countBits(self, n: int) -> List[int]:
        if not n:
            return [0]
        result = [0] * (n + 1)
        result[1] = 1
        
        for i in range(2, n + 1, 1):
            # i is a power of 2
            if (i & (i - 1)) == 0:
                ptr = 0
            result[i] = 1 + result[ptr]
            ptr += 1
                

        return result

        