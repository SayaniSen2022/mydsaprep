# Reverse Nodes in k-Group
# Given the head of a linked list, reverse the nodes of the list k at a time, and return the modified list.
# Input: head = [1,2,3,4,5], k = 2
# Output: [2,1,4,3,5]

class ListNode:
  def __init__(self, val = 0, next = None):
    self.val = val
    self.next = next

class Solution:
  def reverseKGroups(self,head: ListNode,k: int) -> ListNode:
    dummy = ListNode(0, head)
    groupPrev = dummy # for storing the immediate previous node to the start of a group

    while True:
      kth = self.getKth(groupPrev, k)
      if not kth:
        break
      groupNext = kth.next

      # reverse a group
      prev, curr = kth.next, groupPrev.next
      while curr != groupNext:
        tmp = curr.next
        curr.next = prev
        prev = curr
        curr = tmp
      
      tmp = groupPrev.next
      groupPrev.next = kth
      groupPrev = tmp
    
    return dummy.next
    
  def getKth(self, curr, k):
    while curr and k > 0:
      curr = curr.next
      k -= 1
    return curr

