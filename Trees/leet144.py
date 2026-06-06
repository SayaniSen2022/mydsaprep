# BT Preorder Traversal: Given the root of a binary tree, return the preorder traversal of its nodes' values.

from typing import Optional, List

class TreeNode:
  def __init__(self, val=0, left=None, right=None):
    self.val = val
    self.left = left
    self.right = right
class Solution:
  def preorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
    curr = root
    stack = []
    res = []
    while curr or stack:
      if curr:
        res.append(curr.val)
        stack.append(curr.right)
        curr = curr.left
      else:
        curr = stack.pop()
    return res