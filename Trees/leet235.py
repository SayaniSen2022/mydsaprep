# Lowest Common Ancestor of a Binary Search Tree
# Given a binary search tree (BST) where all node values are unique, and two nodes from the tree p and q, return the lowest common ancestor (LCA) of the two nodes.
# The lowest common ancestor between two nodes p and q is the lowest node in a tree T such that both p and q as descendants. The ancestor is allowed to be a descendant of itself.

class TreeNode:
  def __init__(self, val=0, left=None, right=None):
    self.val = val
    self.right = right
    self.left = left

class Solution:
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
       curr = root

       while curr:
          if p.val > curr.val and q.val > curr.val:
             curr = curr.right
          elif p.val < curr.val and q.val < curr.val:
             curr = curr.left
          else:
             return curr