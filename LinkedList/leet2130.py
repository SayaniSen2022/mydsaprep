# Maximum Twin Sum of a Linked List
# In a linked list of size n, where n is even, the ith node (0-indexed) of the linked list is known 
# as the twin of the (n-1-i)th node, if 0 <= i <= (n / 2) - 1.
# For example, if n = 4, then node 0 is the twin of node 3, and node 1 is the twin of node 2. 
# These are the only nodes with twins for n = 4.
# The twin sum is defined as the sum of a node and its twin.
# Given the head of a linked list with even length, return the maximum twin sum of the linked list.]

from typing import Optional

class ListNode:
  def __init__(self, val=0, next=None):
    self.val = val
    self.next = next

class Solution:
  def twinSum(self, head: Optional[ListNode]) -> int:
    if not head:
      return None
    arr = []
    curr = head
    while curr:
      arr.append(curr.val)
      curr = curr.next

    left, right = 0, len(arr) - 1
    res = 0
    while left < right:
      res = max(res, arr[left] + arr[right])
      left, right = left + 1, right - 1

    return res

  def pairSum(self, head: Optional[ListNode]) -> int:
    # fast & slow pointers
    slow, fast = head, head
    while fast and fast.next:
      slow = slow.next
      fast = fast.next.next

    # reverse the second falf
    prev, cur = None, slow
    while cur:
      nxt = cur.next
      cur.next = prev
      prev = cur
      cur = nxt

    res = 0
    first, second = head, prev
    while second:
      res = max(res, first.val + second.val)
      first, second = first.next, second.next # simultaneous iteration of both halves

    return res
