# Min Stack - Design a stack class that supports the push, pop, top, and getMin operations.
# MinStack() initializes the stack object. 
# void push(int val) pushes the element val onto the stack.
# void pop() removes the element on the top of the stack.
# int top() gets the top element of the stack.
# int getMin() retrieves the minimum element in the stack.
# Each function should run in O(1) time.

class MinStack:
  def __init__(self):
    self.stack = []
    self.minStack = []

  def push(self, val: int) -> None:
    # adding value to stack
    self.stack.append(val)
    # comparing to add min val to minstack
    val = min(val, self.minStack[-1] if self.minStack else val)
    self.minStack.append(val)

  def pop(self) -> None:
    self.stack.pop()
    self.minStack.pop()

  def top(self) -> int:
    return self.stack[-1]
  
  def getMin(self) -> int:
    return self.minStack[-1]
