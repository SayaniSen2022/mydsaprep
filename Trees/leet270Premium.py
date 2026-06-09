# Closest Binary Search Tree Value
# Given the root of a binary tree and a target value, return the value in the BST that is closest to the target. If there are
# multiple answers return the smallest
# A BST , all values on left of root will be lower than root, and all values on right of root will be higher than root
# sorted, binary search logic, root mimics the mid point
# we use in-order traversal (its kind of a zigzag binary search list)

import collections
from typing import Optional, List

class TreeNode:
  def __init__(self, val=0, left=None, right=None):
    self.val = val
    self.left = left
    self.right = right

class Solution:
  def closestValue(self, root: Optional[TreeNode], target: float ) -> float:
    closest = root.val
    while root:
      # update closest if current node is nearer to target
      # if equal distance → take the smaller value
      if (abs(root.val - target) < abs(closest - target) or
        (abs(root.val - target) == abs(closest - target) and root.val < closest)):
        closest = root.val

      # BST property — decide direction
      if target < root.val:
        root = root.left
      else:
        root = root.right
    
    return closest


def add_node(node: TreeNode, left: Optional[TreeNode], right: Optional[TreeNode]) -> None:
    if node is None:
        return
    node.left = left
    node.right = right

def build_tree(values: List[Optional[int]]) -> Optional[TreeNode]:
    if not values or values[0] is None:
        return None

    root = TreeNode(values[0])
    q = collections.deque([root])
    i = 1

    while q and i < len(values):
        node = q.popleft()

        left = TreeNode(values[i]) if i < len(values) and values[i] is not None else None
        i += 1
        right = TreeNode(values[i]) if i < len(values) and values[i] is not None else None
        i += 1

        add_node(node, left, right)

        if left: q.append(left)
        if right: q.append(right)

    return root


if __name__ == "__main__":
    s = Solution()

    #        4
    #       / \
    #      2   5
    #     / \
    #    1   3
    root = build_tree([4, 2, 5, 1, 3])
    print(s.closestValue(root, 3.714286))  # Expected: 4
    print(s.closestValue(root, 2.5))       # Expected: 2 (equal dist from 2&3, return smaller)
    print(s.closestValue(root, 1.0))       # Expected: 1
    print(s.closestValue(root, 5.5))       # Expected: 5