# Kth Closest Points to Origin: Given an array of points where points[i] = [xi, yi] represents a point on the X-Y plane 
# and an integer k, return the k closest points to the origin (0, 0).
# The distance between two points on the X-Y plane is the Euclidean distance (i.e., √(x1 - x2)2 + (y1 - y2)2).
# You may return the answer in any order. The answer is guaranteed to be unique (except for the order that it is in).
# Input: points = [[1,3],[-2,2]], k = 1
# Output: [[-2,2]]
# Explanation:
# The distance between (1, 3) and the origin is sqrt(10).
# The distance between (-2, 2) and the origin is sqrt(8).
# Since sqrt(8) < sqrt(10), (-2, 2) is closer to the origin.
# We only want the closest k = 1 points from the origin, so the answer is just [[-2,2]].

from typing import List
import heapq

class Solution:
  def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
    min_heap = []
    for x, y in points:
      # we are not taking the sqrt because technically larger sums will have larger sqrt value, 
      # its kinda redundant here since we only need to compare the distance
      dist = (x**2) + (y**2) 
      min_heap.append([dist, x, y])
    heapq.heapify(min_heap)
    res = []
    while k > 0:
      dist, x, y = heapq.heappop(min_heap)
      res.append([x,y])
      k -= 1
    return res


  def kClosestMaxHeapSol(self, points: List[List[int]], k: int) -> List[List[int]]:
    max_heap = []
    for x, y in points:
      distance = -(x**2 + y**2)
      heapq.heappush(max_heap, [distance, x, y])
      if len(max_heap) > k:
        heapq.heappop(max_heap)
    res = []
    while max_heap:
      distance, x, y = heapq.heappop(max_heap)
      res.append([x, y])
    return res