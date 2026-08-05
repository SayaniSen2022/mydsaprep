# Design HashSet: Design a HashSet without using any built-in hash table libraries.
# Implement MyHashSet class:
# void add(key) Inserts the value key into the HashSet.
# bool contains(key) Returns whether the value key exists in the HashSet or not.
# void remove(key) Removes the value key in the HashSet. If key does not exist in the HashSet, do nothing.

class ListNode:
  def __init__(self, key):
    self.key = key
    self.next = next

class MyHashSet:
  def __init__(self):
    self.set = [ListNode(0) for i in range(10**4)] # max length=10000, array

  def add(self, key: int)  -> None:
    index = key % len(self.set)
    cur = self.set[index]

    while cur.next:
      if cur.next.key == key:
        return
      cur = cur.next
    cur.next = ListNode(key)
  
  def remove(self, key: int) -> None:
    index = key % len(self.set)
    cur = self.set[index]

    while cur.next:
      if cur.next.key == key:
        cur.next = cur.next.next
        return
      cur = cur.next
  
  def contains(self, key: int) -> bool:
    index = key % len(self.set)
    cur = self.set[index]

    while cur.next:
      if cur.next.key == key:
        cur.next = cur.next.next
        return True
      cur = cur.next
    return False