# Same Tree: Given the roots of two binary trees p and q, write a function to check if they are the same or not.
# Two binary trees are considered the same if they are structurally identical, and the nodes have the same value.

class TreeNode:
  def __init__(self, val=0, left=None, right=None):
    self.val = val
    self.left = left
    self.right = right

class Solution:
  def isSameTree(self, p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:
    # both null = same tree
    if not p and not q:
      return True
    # one null one not = not same tree Also if root values mismatch not same tree
    if not p or not q or p.val != q.val:
      return False
    
    # recursion : we need both trees to have similar values to be same tree
    return (self.isSameTree(p.left, q.left) and
    self.isSameTree(p.right, q.right))