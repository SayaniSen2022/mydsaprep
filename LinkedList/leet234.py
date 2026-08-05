# Palindrome Linked List: Given the head of a singly linked list, return true if it is a palindrome or false otherwise.
# Example: Input: head = [1,2,2,1] || Output: True

from typing import Optional

class ListNode:
  def __init__(self, val=0, next=None):
    self.val = val
    self.next = next

class Solution:
  def isPalindrome(self, head: Optional[ListNode]) -> bool:
    if not head: 
      return False
    curr = head
    arr = []

  # traversing the LL and storing the nodes in an array
    while curr:
      arr.append(curr.val)
      curr = curr.next

    # two pointers
    left, right = 0, len(arr) - 1
    while left < right:
      if arr[left] != arr[right]:
        return False
      left += 1
      right -= 1
    return True