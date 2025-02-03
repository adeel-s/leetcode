'''
===#66 Pluse One===
-Input
    List[int] digits: a list of integers representing 
        the digits of a number
        len(digits) is between 1 and 100
        digits[i] is between 0 and 9
-Output
    List[int] the resulting list if 1 is added to the original number

-Observations:
    * Iterate backwards through the array:
        sum = digits[i] + 1 + carry
        if sum > 9:
            digits[i] = sum % 10
            carry = sum / 10
        else: 
            digits[i] = sum
            carry = 0
        
'''
class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        carry = 1

        for i in range(len(digits) - 1, -1, -1):
            sumNums = digits[i] + carry
            print(digits[i], carry, sumNums)
            if sumNums > 9:
                digits[i] = sumNums % 10
                carry = sumNums // 10
            else:
                digits[i] = sumNums
                carry = 0

        if digits[0] == 0:
            digits.insert(0, carry)

        return digits
        