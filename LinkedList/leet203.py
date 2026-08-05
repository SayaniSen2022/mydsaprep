# Remove Linked List Elements: Given the head of a linked list and an integer val, remove all the nodes of the linked 
# list that has Node.val == val, and return the new head.

from typing import Optional
class ListNode:
  def __init__(self, val=0, nexxt=None):
    self.val = val
    self.next = next

class Solution:
  def removeElements(self, head: Optional[ListNode], val: int) -> Optional[ListNode]:
    if not head: 
      return None
    dummy = ListNode(0, head) # create dummy node pointing to head
    prev, curr = dummy, head

    while curr:
      if curr.val == val:
        prev.next = curr.next
      else:
        prev = curr
      curr = curr.next
    return dummy.next
