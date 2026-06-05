# Left and Right Sum Differences: You are given a 0-indexed integer array nums of size n.
# Define two arrays leftSum and rightSum where:
# leftSum[i] is the sum of elements to the left of the index i in the array nums. If there is no such element, leftSum[i] = 0.
# rightSum[i] is the sum of elements to the right of the index i in the array nums. If there is no such element, rightSum[i] = 0.
# Return an integer array answer of size n where answer[i] = |leftSum[i] - rightSum[i]|.
# Example: Input: nums = [10,4,8,3] Output: [15,1,11,22]

from typing import List

class Solution:
  def leftRightDifference(self, nums: List[int]) -> int:
    left_sum = 0
    leftSum = []
    rightSum = []
    res = []
    for i in range(len(nums)):
      if i == 0:
        left_sum = 0
        leftSum.append(left_sum)
      else:
        left_sum += nums[i - 1]
        leftSum.append(left_sum)
      
      right_sum = 0
      for j in range((i+1),len(nums)):
        right_sum += nums[j]
      rightSum.append(right_sum)

    for k in range(len(nums)):
      res.append(abs(leftSum[k] - rightSum[k]))
    return res
  
if __name__ == "__main__":
  s = Solution()
  print(s.leftRightDifference([10, 4, 8, 3]))  # Expected: [15, 1, 11, 22]
  print(s.leftRightDifference([1]))  

  # optimal solution: prefix calculation O(n)
  def leftRightDiff(self, nums: List[it]) -> int:
    total = sum(nums)
    left_sum = 0
    res = []

    for num in nums:
      right_sum = total - left_sum - num
      res.append(abs(left_sum - right_sum))
      left_sum += num
    return res