# Intersection of Two Linked Lists: Given the heads of two singly linked-lists headA and headB, return the node 
# at which the two lists intersect. If the two linked lists have no intersection at all, return null.

from typing import Optional

class ListNode:
  def __init__(self, val=0, next=None):
    self.val = val
    self.next= next

class Solution:
  def getIntersectionNode(self, head1: Optional[ListNode], head2: Optional[ListNode]) -> Optional[ListNode]:
    nodeSet = set()
    cur = head1
    while cur:
      nodeSet.add(cur)
      cur = cur.next

    cur = head2
    while cur:
      if cur in nodeSet:
        return cur
      cur = cur.next

    return None
