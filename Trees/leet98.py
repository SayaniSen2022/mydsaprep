# Valid BST: Given the root of a binary tree, determine if it is a valid binary search tree (BST).

from typing import Optional

class TreeNode:
  def __init__(self, val=0, left=None, right=None):
    self.val = val
    self.left = left
    self.right = right

class Solution:
  def isValidBST(self, root: Optional[TreeNode]) -> bool:
    def valid(node : Optional[TreeNode], left_boundary: float, right_boundary: float):
      if not node:
        return True # empty bt is also considered a valid bst
      if not (node.val > left_boundary and node.val < right_boundary):
        return False
      
      return (valid(node.left, left_boundary, node.val) and valid(node.right, node.val, right_boundary))
    return valid(root, float("-inf"), float("inf"))
