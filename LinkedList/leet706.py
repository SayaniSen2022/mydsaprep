# Design HashMap: Design a HashMap without using any built-in hash table libraries.
# Implement the MyHashMap class:
# MyHashMap() initializes the object with an empty map.
# void put(int key, int value) inserts a (key, value) pair into the HashMap. If the key already exists in the map, update the corresponding value.
# int get(int key) returns the value to which the specified key is mapped, or -1 if this map contains no mapping for the key.
# void remove(key) removes the key and its corresponding value if the map contains the mapping for the key.

class ListNode:
  def __init__(self, key=-1, val=-1, next=None):
    self.key = key
    self.val = val
    self.next = next

class MyHashMap:
  def __init__(self):
    self.map = [ListNode() for i in range(1000)]

  def hash(self, key: int):
    return key % len(self.map)

  def put(self, key: int, value: int) -> None:
    cur = self.map[self.hash(key)] # mapping the key
    # since first node is dummy
    while cur.next:
      # if key already exists we update only the value
      if cur.next.key == key:
        cur.next.val = value
        return
      cur = cur.next
    cur.next = ListNode(key, value)


  def get(self, key: int) -> int:
    cur = self.map[self.hash(key)].next
    while cur:
      if cur.key == key:
        return cur.val
      cur = cur.next
    return -1
  
  def remove(self, key: int) -> None:
    cur = self.map[self.hash(key)]
    while cur and cur.next:
      if cur.next.key == key:
        cur.next = cur.next.next
        return
      cur = cur.next