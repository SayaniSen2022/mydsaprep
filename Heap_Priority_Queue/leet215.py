# Kth largest element

from typing import List
import heapq

class Solution:
  def findKthLargest(self, nums: List[int], k: int) -> int:
    max_heap = [-n for n in nums]
    heapq.heapify(max_heap)
    res = []
    counter = 0

    while max_heap:
      val = heapq.heappop(max_heap)
      counter +=1
      if counter == k:
        return -(val)