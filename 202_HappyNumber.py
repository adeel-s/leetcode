'''
===#202 Non-Cyclical Number===
-Input
    int n: an integer
-Output
    bool result: whether n is cyclical or not
-Complexity
    ?
-Observations
    * A cycle can be detected by 
        * a set
        * a fast/slow pointer
            if the fast pointer reached 1, non-cyclical
            else, cyclical
        
-Solution
    Create a set to store sums of digit squares

    while n !=1 and n isn't in s:
        add n to s
        while n has digits left:
            add the digit square to a summing variable
        n = summing variable
    return whether n == 1
'''
class Solution:
    def isHappy(self, n: int) -> bool:
        s = set()
        while n != 1 and n not in s:
            s.add(n)
            digSum = 0
            while n > 0:
                digSum += pow(n % 10, 2)
                n = n // 10
            n = digSum
        
        return n == 1
        