'''
===#190 Reverse Bits===
-Input
    int n: a 32 bit unsigned integer

-Output
    int result: the bit-wise compliment of n

-Observations
    * Which binary bitwise operator, given 0 (or 1) as an operand, will
        flip all of n's bits?
        * XOR 1: 
            1 ^ 1 = 0
            0 ^ 1 = 1
    * Proposal:
        while n:
            result += (n % 2) ^ 1
            result << 2
            n >> 2
'''
class Solution:
    def reverseBits(self, n: int) -> int:
        result = 0
        bits = 32
        for i in range (bits):
            bit = (n >> i) & 1
            result |= (bit << (bits - i - 1))

        return result



        