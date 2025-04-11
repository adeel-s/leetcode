class Solution:
    def countSymmetricIntegers(self, low: int, high: int) -> int:
        result = 0
        for i in range(low, high+1, 1):
            num = str(i)
            if len(num) % 2 == 1:
                continue
            first = num[0:len(num)//2]
            last = num[len(num)//2:]
            firstSum = 0
            lastSum = 0
            for digit in first:
                firstSum += int(digit)
            for digit in last:
                lastSum += int(digit)
            result += 1 if firstSum == lastSum else 0

        return result
        