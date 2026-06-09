# Binary Tree Paths: Given the root of a binary tree, return all root-to-leaf paths in any order.
# A leaf is a node with no children.

from typing import Optional, List
import collections

class TreeNode:
  def __init__(self, val=0, left=None, right=None):
    self.val = val
    self.right = right
    self.left = left

class Solution:
  def binaryTreePaths(self, root: Optional[TreeNode]) -> List[int]:
    res = [] # main output
    def dfs(node, path):
      if not node:
        return
      
      path += str(node.val)

      # check for leaf node
      if not node.left and not node.right:
        res.append(path)
        return
      
      # recursion
      dfs(node.left, path + "->")
      dfs(node.right, path + "->")
    dfs(root, "")
    return res
  

# adding node

def add_node(node: TreeNode, left: TreeNode, right: TreeNode) -> None:
    if node is None:
      return 

    node.left = left
    node.right = right

# building a tree
def build_tree(values: List[Optional[int]]) -> Optional[TreeNode]:
  if not values or values[0] is None:
    return None
  
  root = TreeNode(values[0])
  q = collections.deque([root])
  i = 1

  while q and i < len(values):
    node = q.popleft()

    # adding left child first
    left = TreeNode(values[i]) if i < len(values) and values[i] is not None else None
    i += 1

    # adding right child
    right = TreeNode(values[i]) if i < len(values) and values[i] is not None else None
    i += 1

    add_node(node, left, right) # helper function to build node

    if left: q.append(left)
    if right: q.append(right)
  
  return root



if __name__ == "__main__":
  root = build_tree([1,2,3,None,5])
  print(Solution().binaryTreePaths(root))
