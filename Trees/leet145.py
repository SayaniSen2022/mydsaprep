# PostOrder Traversal

from typing import Optional, List

class TreeNode:
  def __init__(self, val=0,left=None, right=None):
    self.val = val
    self.right = right
    self.left = left

class Solution:
  def postOrderTraversal(self, root: Optional[TreeNode]) -> List[int]:
    stack = [root] # tracks the nodes
    res = []
    visit= [False] # tracks whether a node has been already visited, since we add only twice visited nodes to our res

    while stack:
      cur, v = stack.pop(), visit.pop()
      if cur:
        if v:
          res.append(cur.val)
        else:
          stack.append(cur)
          visit.append(True) # since visiting curr, hence true
          # right and left nodes still not visited, so False
          # we add right at first, then left, since we want to visit left, then right, then root
          stack.append(cur.right)
          visit.append(False)
          stack.append(cur.left)
          visit.append(False)
    return res