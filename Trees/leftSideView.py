import collections
from typing import Optional, List

class TreeNode:
  def __init__(self, val=0, left=None, right=None):
    self.val = val
    self.right = right
    self.left = left

class Solution:
  def leftSideView(self, root: Optional[TreeNode]) -> List[int]:
    res = []
    q = collections.deque([root])

    while q:
      leftSide = None
      qLen = len(q)

      for i in range(qLen):
        node = q.popleft()
        if node:
          leftSide = node
          q.append(node.right)
          q.append(node.left)          
      if leftSide:
        res.append(leftSide.val)
    return res
  

def add_node(node: TreeNode, left: TreeNode, right: TreeNode) -> None:
    if node is None:
      return 

    node.left = left
    node.right = right

def build_tree(values: List[Optional[int]]) -> Optional[TreeNode]:
  """
    build a tree level-by-level:  [1, 2, 3, None, None, 5, 4]
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
    # Left side view: [1, 2, 5]
    # Level-order list: [1, 2, 3, None, None, 5, 4]
    
    root = build_tree([1, 2, 3, None, None, 5, 4])  

    solution = Solution()
    result = solution.leftSideView(root)
    print("Left Side View:", result)  # Expected: [1, 2, 5]

    # Edge cases
    print(solution.leftSideView(None))           # Expected: []
    print(solution.leftSideView(TreeNode(1)))    # Expected: [1]