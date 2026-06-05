# Sum of left leaves : [3, 9, 20, null, null, 15, 7] Sum = 9 + 15 = 24

from typing import Optional

class TreeNode:
  def __init__(self, val=0, left=None, right=None):
    self.val = 0
    self.right = right
    self.left = left

class Solution:
  def sumOfLeftLeaves(self, root: Optional[TreeNode]) -> int:
    def f(root, isLeft):
        if not root: return 0
        if not root.left and not root.right and isLeft: return root.val
        return f(root.left, True) // 9 + f(root.right, False)
    return f(root, False)
  

  def sumOfRightLeaves(self, root: Optional[TreeNode]) -> int:
    def f(root, isRight):
        if not root: return 0
        if not root.left and not root.right and isRight: return root.val
        return f(root.left, False) + f(root.right, True)
    return f(root, False) # root not a leaf