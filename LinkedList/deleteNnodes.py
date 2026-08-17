# The problem asks us to keep the first m nodes, then delete the next n nodes, and repeat this pattern throughout 
# the linked list. Return the head of the modified list.
# Prerequisites: Linked List Traversal, Pointer Manipulation, In-Place Modification
# TC: O(n); SC: O(1)

from typing import Optional

class ListNode:
  def __init__(self, val=0, next=None):
    self.val = val
    self.next = next

class Solution:
  def deleteNodes(self, head: Optional[ListNode], m: int, n: int) -> Optional[ListNode]:
    # initialize both the current node and the mth node to be head
    curr_node = head
    last_m_node = head

    while curr_node:
      # initialize m_count to m and n_count to n
      m_count, n_count = m, n

      # traverse m node
      while curr_node and m_count != 0:
        last_m_node = curr_node
        curr_node = curr_node.next
        m_count -= 1

       # traverse n nodes
      while curr_node and n_count != 0:
        curr_node = curr_node.next
        n_count -= 1

      # delete n nodes  
      last_m_node.next = curr_node

    return head