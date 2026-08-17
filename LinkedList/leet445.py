# Add Two Numbers II: You are given two non-empty linked lists representing two non-negative integers. 
# The most significant digit comes first and each of their nodes contains a single digit. 
# Add the two numbers and return the sum as a linked list.
# You may assume the two numbers do not contain any leading zero, except the number 0 itself.

from typing import Optional

class ListNode:
  def __init__(self, val=0, next=None):
    self.val = val
    self.next = next

class Solution:
  def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
    s1, s2 = [], []

    while l1:
      s1.append(l1.val)
      l1 = l1.next
    while l2:
      s2.append(l2.val)
      l2 = l2.next

    carry = 0
    head = None

    while s1 or s2 or carry:
      v1 = s1.pop() if s1 else 0
      v2 = s2.pop() if s2 else 0
      total = v1 + v2 + carry
      carry = total // 10
      node = ListNode(total % 10)
      node.next = head
      head = node

    return head