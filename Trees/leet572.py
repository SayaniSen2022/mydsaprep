# Subtree of Another Tree: Given the roots of two binary trees root and subRoot, 
# return true if there is a subtree of root with the same structure and node values of subRoot and false otherwise.
# A subtree of a binary tree tree is a tree that consists of a node in tree and all of this node's descendants. 
# The tree tree could also be considered as a subtree of itself.

class TreeNode:
  def __init__(self, val=0, left=None, right=None):
    self.val = val
    self.right = right
    self.left = left

class Solution:
  def isSubtree(self, s: TreeNode, t: TreeNode) -> bool:
    if not t: return True
    if not s: return False
    if self.isSametree(s, t):
      return True
    
    return (self.isSubtree(s.left, t) or self.isSubtree(s.right, t))

  def isSametree(self, s, t):
    if not s and not t:
      return True
    
    if s and t and s.val == t.val:
      return (self.isSametree(s.left, t.left) and
      self.isSametree(s.right, t.right))
    return False