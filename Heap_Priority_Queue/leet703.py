# Design a class to find the kth largest integer in a stream of values, including duplicates. 
# E.g. the 2nd largest from [1, 2, 3, 3] is 3. The stream is not necessarily sorted.
# Implement the following methods:
# constructor(int k, int[] nums) Initializes the object given an integer k and the stream of integers nums.
# int add(int val) Adds the integer val to the stream and returns the kth largest integer in the stream.

from typing import List
import heapq

class kthLargest:
  def __init__(self, k: int, nums: List[int]):
    # minheap with k largest integers
    self.min_heap, self.k = nums, k
    heapq.heapify(self.min_heap)
    while len(self.min_heap) > k:
      heapq.heappop(self.min_heap)


  def add(self, val: int) -> int:
    heapq.heappush(self.min_heap, val)
    if len(self.min_heap) > self.k:
      heapq.heappop(self.min_heap)
    return self.min_heap[0]