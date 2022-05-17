"""
Q155. Min Stack
https://leetcode.com/problems/min-stack/

Design a stack that supports push, pop, top, and retrieving the minimum element in constant time.

Implement the MinStack class:

MinStack() initializes the stack object.
void push(int val) pushes the element val onto the stack.
void pop() removes the element on the top of the stack.
int top() gets the top element of the stack.
int getMin() retrieves the minimum element in the stack.

"""

class MinStack:

    def __init__(self):
        self.stack = []
        self.minimum = []
        

    def push(self, val: int) -> None:
        self.stack.append(val)
        if len(self.minimum) == 0:
            self.minimum.append(val)
        else:
            if val <= self.minimum[-1]:
                self.minimum.append(val)

    def pop(self) -> None:
        numPop = self.stack[-1]   
        if self.minimum[-1] == numPop:
            self.minimum.pop()
        self.stack.pop(-1)
        

    def top(self) -> int:
        return self.stack[-1]
        

    def getMin(self) -> int:
        return self.minimum[-1]
        


# Your MinStack object will be instantiated and called as such:
# obj = MinStack()
# obj.push(val)
# obj.pop()
# param_3 = obj.top()
# param_4 = obj.getMin()