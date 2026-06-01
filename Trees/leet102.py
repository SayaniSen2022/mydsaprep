# Binary Tree Level Order Traversal
# Given a binary tree root, return the level order traversal of it as a nested list, 
# where each sublist contains the values of nodes at a particular level in the tree, from left to right.

import collections
from typing import Optional, List

class TreeNode:
  def __init__(self, val=0, left=None, right=None):
    self.val = val
    self.right = right
    self.left = left

class Solution:
  def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
    # breadth first search : queue
    res = []
    q = collections.deque()
    q.append(root)

    while q:
      qLength = len(q)
      level = []
      for i in range(qLength):
        node = q.popleft()
        if node:
          level.append(node.val)
          q.append(node.left)
          q.append(node.right)
      # checking that the level is non-empty    
      if level:
        res.append(level)
    return res

