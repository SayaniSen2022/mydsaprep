# Valid Parentheses: Given a string s containing just the characters '(', ')', '{', '}', '[' and ']', determine if the input string is valid.
# An input string is valid if:
# Open brackets must be closed by the same type of brackets.
# Open brackets must be closed in the correct order.
# Every close bracket has a corresponding open bracket of the same type.


class Solution:
  def isValid(self, s: str) -> bool:
    # edge case: we cannot start with a closinh parenthesis

    stack = []
    # hashmap to set each close to its corresponding open parenthesis
    closeToOpen = {")":"(", "]":"[", "}": "{"} # keys are closing parenthesis

    for c in s:
      if c in closeToOpen:
        if stack and stack[-1] == closeToOpen[c]: # [-1] refers to the element on top of the stack
          stack.pop()
        else:
          return False
      else:
        stack.append(c)
    return True if not stack else False        
