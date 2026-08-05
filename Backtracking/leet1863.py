# Sum of All Subsets XOR Total

from typing import List

class Solution:
  def subsetXORSum(self, nums: List[int]) -> int:
    def dfs(i, total):
      if i == len(nums):
        return total
      
      # include nums[i] + not include nums[i]
      return dfs(i + 1, total ^ nums[i]) +  dfs(i + 1, total)
    return dfs(0, 0)
