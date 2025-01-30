'''
===#22 Generate Parentheses===
-Input
    int n: a number of well-formed parentheses
        n is between 1 and 7
-Output
    List[str] result: strings of all possible pairs of n parentheses

-Complexity
    O(4^n/√n) time
    O(n) space

-Observations
    * Brute force:
        Keep a set of unique strings
            n times:
                convert the set to a list
                For each string in the list:
                    For each character in the string:
                        insert "()" before/after the character
                        Add to the set
                This becomes the set I use for the next iteration

'''
class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        stack = []
        result = []

        def backtrack(opens, closes):
            if opens == closes == n:
                result.append("".join(stack))
                return

            if opens < n:
                stack.append("(")
                backtrack(opens + 1, closes)
                stack.pop()

            if closes < opens:
                stack.append(")")
                backtrack(opens, closes + 1)
                stack.pop()

        backtrack(0, 0)
        return result
        