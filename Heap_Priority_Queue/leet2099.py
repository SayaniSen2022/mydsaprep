# Find Subsequence of Length K with the Largest Sum
# You are given an integer array nums and an integer k. You want to find a subsequence of nums of length k that has the largest sum.
# Return any such subsequence as an integer array of length k.
# A subsequence is an array that can be derived from another 
# array by deleting some or no elements without changing the order of the remaining elements.
# Input:  nums=[2,1,3,3]

from typing import List
import heapq

class Solution:
  def maxSubsequence(self, nums: List[int], k: int) -> List[int]:
    max_heap = [(-n, i) for i, n in enumerate(nums)]
    heapq.heapify(max_heap) 
    res = []

    while k:
      val, idx = heapq.heappop(max_heap) # heappop removes and returns the smallest element from a minheap
      res.append((idx, val))
      k -= 1
    # print(res)
    res.sort(key=lambda x:x[0])
    # print(res)
    return [-val for idx, val in res]

if __name__ == "__main__":
  nums = [-1,-2,3,4]
  sol = Solution()
  result = sol.maxSubsequence(nums, 3)
  print(result)
