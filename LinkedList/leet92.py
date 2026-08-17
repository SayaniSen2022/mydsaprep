# Reverse Linked List II: Given the head of a singly linked list and two integers left and right where left <= right, 
# reverse the nodes of the list from position left to position right, and return the reversed list.

from typing import Optional

class ListNode:
  def __init__(self, val=0, next=None):
    self.val = 0
    self.next = next

class Solution:
  def reverseBetween(self, head: Optional[ListNode], left: int, right: int) -> Optional[ListNode]:
    dummy = ListNode(0, head)

    # to reach node position "left"
    leftPrev, cur = dummy, head
    for i in range(left - 1):
      leftPrev, cur = cur, cur.next

    # Now cur = "left",leftPrev = "node before left"
    # reverse from left to right
    prev = None
    for i in range(right - left + 1):
      tmpNext = cur.next
      cur.next = prev
      prev, cur = cur, tmpNext

    # Update pointers
    leftPrev.next.next = cur # cur is the node after "right"
    leftPrev.next = prev # prev is "right" node

    return dummy.next