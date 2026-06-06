# Count Complete BT Nodes: A complete BT has:
# A perfect binary tree of height h has exactly 2^h - 1 nodes
# You can measure the leftmost height and rightmost height in O(log n)
# If they're equal → it's a perfect subtree → use the formula, no need to traverse

from typing import Optional

class TreeNode:
  def __init__(self, val=0, left=None, right=None):
    self.val = val
    self.left = left
    self.right = right

class Solution:
  def countNodes(self, root: Optional[TreeNode]) -> int:
    if not root:
      return 0
    
    left_height, right_height = 0, 0
    left = root
    right = root

    # calculate height of leftmost path
    while left:
      left_height += 1
      left = left.left

    # calculate height of rightmost path
    while right:
      right_height += 1
      right = right.right

    # if equal → perfect binary tree → use formula = No. of nodes = (2^h - 1)
    if left_height == right_height:
      return ( 2 ** left_height) - 1 # O(1)
    
    # if not equal → recurse on subtrees 
    return 1 + self.countNodes(root.left) + self.countNodes(root.right)
  