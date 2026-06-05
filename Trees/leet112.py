# Path Sum: Given the root of a binary tree and an integer targetSum, 
# return true if the tree has a root-to-leaf path such that adding up all the values along the path equals targetSum.

from typing import Optional

class TreeNode:
  def __init__(self, val=0, left=None, right=None):
    self.val = val
    self.left = left
    self.right = right

class Solution:
  def hasPathSum(self, targetSum: int, root: Optional[TreeNode]) -> bool:
    # in-order(root, left, right) depth first search DFS
    def dfs(node, curr_sum):
      # edge case for empty tree
      if not node:
        return False
      curr_sum += node.val # calculation of path sum
      # check for leaf node
      if not node.left and not node.right:
        return curr_sum == targetSum # will return true only if condition satisfies
      # will return true if either is true
      return(dfs(node.left, curr_sum) or dfs(node.right, curr_sum))
    return dfs(root, 0)