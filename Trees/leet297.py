# Serialize And Deserialize Binary Tree: Implement an algorithm to serialize and deserialize a binary tree.

# Serialization is the process of converting an in-memory structure into a sequence of bits so that it can be stored or 
# sent across a network to be reconstructed later in another computer environment.
# You just need to ensure that a binary tree can be serialized to a string and 
# this string can be deserialized to the original tree structure. There is no additional restriction on how your 
# serialization/deserialization algorithm should work.

from typing import Optional

class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Codec:
    def serialize(self, root: Optional[TreeNode]):
        res = []
        def dfs(node):
          if not node:
              res.append("N")
              return
          res.append(str(node.val))
          dfs(node.left)
          dfs(node.right)
        dfs(root)
        return ",".join(res)
    
    # Decode encoded data to tree
    def deserialize(self, data: str) -> Optional[TreeNode]:
        vals = data.split(",")
        self.i = 0

        def dfs():
            if vals[self.i] == "N":
                self.i += 1
                return None
            node = TreeNode(int(vals[self.i]))
            self.i += 1
            node.left = dfs()
            node.right = dfs()
            return node
        return dfs()
