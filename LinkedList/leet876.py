# Middle of the Linked List: Given the head of a singly linked list, return the middle node of the linked list.
# If there are two middle nodes, return the second middle node.

from typing import Optional

class ListNode:
  def __init__(self, vaal=0, nexxt=None):
    self.val = self.val
    self.next = next

class Solution:
  def middleNode(self, head: Optional[ListNode]) -> Optional[ListNode]:
    if not head:
      return None
    fast, slow = head, head
    while fast and fast.next:
      fast = fast.next.next
      slow = slow.next
    return slow