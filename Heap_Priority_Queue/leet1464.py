# Maximum Products of 2 Elements in an Array
# Given the array of integers nums, you will choose two different indices i and j of that array. 
# Return the maximum value of (nums[i]-1)*(nums[j]-1).
# Example: Input: nums = [3,4,5,2] Output: 12
# Because 4 and 5 are the 2 largest numbers in the array, we deduct 1 from each and get the max product.

from typing import List
import heapq

class Solution:
  def maxProduct(self, nums: List[int]) -> int:
    max_heap = [-n for n in nums]
    heapq.heapify(max_heap) # [-5, -4, -3, -2]

    first = abs(heapq.heappop(max_heap))
    second = abs(heapq.heappop(max_heap))
    return (first - 1) * (second - 1)


if __name__ == "__main__":
  nums = [1,5,4,5]
  sol = Solution()
  result = sol.maxProduct(nums)
  print(result)