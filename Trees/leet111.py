# Minimum Depth of a BT
# Given a binary tree, find its minimum depth.
# The minimum depth is the number of nodes along the shortest path from the root node down to the nearest leaf node.
# Note: A leaf is a node with no children.

from typing import Optional

class TreeNode:
  def __init__(self, val=0, left=None, right=None):
    self.val = val
    self.left = left
    self.right = right

class Solution:
  def minDepth(self, root: Optional[TreeNode]) -> int:
    # recursion
    if not root:
        return 0
    leftDepth = self.minDepth(root.left)
    rightDepth = self.minDepth(root.right)
    if leftDepth == 0:
        return 1 + rightDepth
    elif rightDepth == 0:
        return 1  + leftDepth
    else:
        return 1 + min(leftDepth, rightDepth)
        