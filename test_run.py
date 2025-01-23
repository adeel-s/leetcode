class Solution:
    def isHappy( n: int) -> bool:
        s = set()
        while n != 1 and n not in s:
            digSum = 0
            while n > 0:
                digSum += pow(n % 10, 2)
                n = n // 10
            n = digSum
            s.add(n)
        
        return n == 1
    print(isHappy(101))