# Binary Tree Right Side View: You are given the root of a binary tree. Return only the values of the nodes 
# that are visible from the right side of the tree, ordered from top to bottom.

import collections
from typing import Optional, List

class TreeNode:
  def __init__(self, val=0, left=None, right=None):
    self.val = val
    self.right = right
    self.left = left

class Solution:
  def rightSideView(self, root: Optional[TreeNode]) -> List[int]:
    res = []
    q = collections.deque([root])

    while q:
      rightSide = None
      qLen = len(q)

      for i in range(qLen):
        node = q.popleft()
        if node:
          rightSide = node
          q.append(node.left)
          q.append(node.right)
      if rightSide:
        res.append(rightSide.val)
    return res
  

def add_node(node: TreeNode, left: TreeNode, right: TreeNode) -> None:
    if node is None:
      return 

    node.left = left
    node.right = right

def build_tree(values: List[Optional[int]]) -> Optional[TreeNode]:
  """
    build a tree level-by-level:  [1, 2, 3, None, 5, None, 4]
  """
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


# --- Test Script ---
if __name__ == "__main__":
    # Build this tree:
    #         1
    #        / \
    #       2   3
    #        \    \
    #         5    4
    # Right side view: [1, 3, 4]
    # Level-order list: [1, 2, 3, None, 5, None, 4]
    
    root = build_tree([1, 2, 3, None, 5, None, 4])  

    solution = Solution()
    result = solution.rightSideView(root)
    print("Right Side View:", result)  # Expected: [1, 3, 4]

    # Edge cases
    print(solution.rightSideView(None))           # Expected: []
    print(solution.rightSideView(TreeNode(1)))    # Expected: [1]