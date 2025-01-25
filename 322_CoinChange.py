'''
===#322 Coin Change===

-Input
    List[int] coins: a list of coin denominations
        len(coins) is between 1 and 10
        coins[i] is between 1 and int.MAX_LENGTH
    int amount: an amount that coins in coins must be added to
        amount is between 0 and 10,000

-Output
    int result: the minimum number of coins needed to reach the target
        -1 if the amount can't be made exactly

-Complexity
    O(nt) time
    O(t) space
    where 
        n is the number of coins
        t is the given amount

-Observations
    * A greedy solution works:
        Subtract the highest denomination from amount
            until amount = 0
            If this isn't possible, return -1
    * Coins has to be sorted... but this is O(100) I think that's okay
    * Proposal:
        Sort coins in descending order
        while amount > 0:
            try subtracting each coin from amount without it going negative
                Once you succeed, stop trying with lower coins
    * This fails: greedy doesn't always work:
        Coins: [11, 22, 33, 44, 55, 66, 77, 88, 99, 111]
        Amount: 330
            Greedy solution takes 111, 111, 99, and then reaches the end without 
                finding the solution: 66, 77, 88, 99
    * With O(t) space, I could store values from 0 to amount,
        storing a solution for each number
    * If I compute solutions to all numbers up to amount,
        when I get to amount, I will know whether each number before it
            has a solution
    * Proposal:
        create a dictionary with values from 0 to amount
            from 0 to amount:
                # check for base case: the number has a corresponding coin denomination
                for num in nums:
                    if num - i == 0:
                        push i:1
                for num in nums:
                        if dictionart.get(i-num):
                            push min(dictionary.get(i-num),i-num:dictionart.get(i-num) + 1)

-Solution
    numCoins = {0:0}

    for i in range(1, amount + 1, 1):
        for num in nums:
            if num - i == 0:
                numCoins[i] = 1
            else:
                if numCoins.get(i - num):
                    numCoins[i] = min(numCoins[i],numCoins[i-num] + 1)
    return -1 if not numCoins[amount] else numCoins[amount]


'''
class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        numCoins = {0:0}
        print(numCoins.get(amount))
        for i in range(1, amount + 1, 1):
            for num in coins:
                if num - i == 0:
                    numCoins[i] = 1
                else:
                    if numCoins.get(i - num):
                        numCoins[i] = numCoins[i-num] + 1 if not numCoins.get(i) else min(numCoins.get(i), numCoins[i-num] + 1)
        if amount == 0:
            return 0
        return -1 if not numCoins.get(amount) else numCoins[amount]








        