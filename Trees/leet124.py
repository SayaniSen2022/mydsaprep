# Binary Tree Maximum Path Sum: Given the root of a non-empty binary tree, return the maximum path sum of any non-empty path.
# A path in a binary tree is a sequence of nodes where each pair of adjacent nodes has an edge connecting them. 
# A node can not appear in the sequence more than once. The path does not necessarily need to include the root.
# The path sum of a path is the sum of the node's values in the path.

from typing import Optional

class TreeNode:
  def _init__(self, val=0, left=None, right=None):
    self.val = 0
    self.left = left
    self.right = right

class Solution:
  def maxPathSum(self, root: Optional[TreeNode]) -> int:
    res = [root.val]

    # recursive dfs: return max path sum without split
    def dfs(root):      
      # edge case
      if not root:
        return 0
      
      leftMax = dfs(root.left)
      rightMax = dfs(root.right)

      # update them in case they are negative, we do not want to add negative values while returning max path
      leftMax = max(leftMax, 0)
      rightMax = max(rightMax, 0)

      # max path sum with split
      res[0] = max(res[0], (root.val + leftMax + rightMax))

      # return max path sum without split
      return root.val + max(leftMax, rightMax)
    
    dfs(root)
    return res[0]