'''
===#155 Minimum Stack===

Design a stack class that supports the following functions:
    MinStack() initializes the stack object.
    void push(int val) pushes the element val onto the stack.
    void pop() removes the element on the top of the stack.
    int top() gets the top element of the stack.
    int getMin() retrieves the minimum element in the stack.
Each function should run in constant time

-Observations
    * Most standard python stack behavior can be used for methods other than getMin()
        However:
        pop() does not return a value
        top() returns a value without popping (peeking)

    * getMin() can be implemented by storing a minStack to track the minimum value
        at each state of the stack
        * When an element is pushed, minStack stores the minimum of the last min and
            the incoming value
        * On a pop, if the stack and minStack are both popped, minStack will then
            have the previous minimum at the top of the stack.

'''
class MinStack:

    def __init__(self):
        self.stack = []
        self.minStack = []

    def push(self, val: int) -> None:
        self.stack.append(val)
        if self.minStack:
            self.minStack.append(min(self.minStack[len(self.minStack)-1], val))
        else:
            self.minStack.append(val)

    def pop(self) -> None:
        self.stack.pop()
        self.minStack.pop()

    def top(self) -> int:
        return self.stack[len(self.stack) - 1]

    def getMin(self) -> int:
        return self.minStack[len(self.minStack) - 1]
        
