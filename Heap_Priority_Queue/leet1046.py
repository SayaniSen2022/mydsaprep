# Last Stone Weight: You are given an array of integers stones where stones[i] represents the weight of the ith stone.
# We want to run a simulation on the stones as follows:
# At each step we choose the two heaviest stones, with weight x and y and smash them togethers
# If x == y, both stones are destroyed
# If x < y, the stone of weight x is destroyed, and the stone of weight y has new weight y - x.
# Continue the simulation until there is no more than one stone remaining.
# Return the weight of the last remaining stone or return 0 if none remain.

# python does not have max heap, so we use min heap to simulate the max heap by multiplying weight of each stone with -1

from typing import List
import heapq

class Solution:
  def lastStoneWeight(self, stones: List[int]) -> int:
    stones = [-s for s in stones]
    heapq.heapify(stones)

    # since we need to compare 2 weights, loop breaks when only 1 element is left
    while len(stones) > 1:
      first = heapq.heappop(stones)
      second = heapq.heappop(stones)

      # since we have made the stone negative value for python, second val will be greater
      if second > first:
        heapq.heappush(stones, first - second) # first - second will take care of the -ve, no need to add abs function
      
    stones.append(0) # incase no stones left once loop is complete, we return 0
    return abs(stones[0])