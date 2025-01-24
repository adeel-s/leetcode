'''
===#150 Reverse Polish Notation===
-Input
    List[str] tokens: a valid arithmetic expression in
        postfix notation
        len(tokens) is between 1 and 1000
        tokens[i] is an arithmetic operator or integer between
        -100 and 100 in string form
-Output
    int result: the result of evaluating the postfix expression

-Complexity
    O(n) time, space

-Observations
    * A stack will be useful for this
        If token is an int, push onto the stack
        If it's an operator, pop, pop, apply operator, push
    * isdigit()
    * one case for each operator...?
'''
class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        operands = []
        print(-133//6)
        for token in tokens:
            print(operands)
            if token.isdigit() or token[1:].isdigit():
                operands.append(int(token))
            else:
                rhs = operands.pop()
                lhs = operands.pop()
                if token == "+":
                    lhs = lhs + rhs
                elif token == "-":
                    lhs = lhs - rhs
                elif token == "*":
                    lhs = lhs * rhs
                else:
                    if rhs == 0:
                        lhs = 0
                    else:
                        sign = lhs * rhs
                        lhs = abs(lhs) // abs(rhs)
                        lhs *= 1 if sign >=0 else -1
                        print(lhs)
                operands.append(lhs)

        return operands.pop()

        