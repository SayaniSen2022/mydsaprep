# Copy List with Random Pointer
# A linked list of length n is given such that each node contains an additional random pointer, which could point to any node in the list, or null.
# Construct a deep copy of the list.

class Node:
  def __init__(self, x:int, next: 'Node' = None, random: 'Node' = None):
    self.val = int(x)
    self.next = next
    self.random = random

class Solution:
  def copyRandomList(Self, head: 'Optional[Node]') -> 'Optional[Node]':
    oldToCopy = { None: None }

    #first pass : copying the values from old linklist to hashmap
    curr = head
    while curr:
      copy = Node(curr.val)
      oldToCopy[curr] = copy
      curr = curr.next

    #second pass, for pointers
    curr = head
    while curr:
      copy = oldToCopy[curr]
      copy.next = oldToCopy[copy.next]
      copy.random = oldToCopy[copy.random]
      curr = curr.next
    return oldToCopy[head]