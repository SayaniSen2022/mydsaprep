# Find the Duplicate Number
#Given an array of integers nums containing n + 1 integers where each integer is in the range [1, n] inclusive.
# There is only one repeated number in nums, return this repeated number.

class Solution:
  def findDuplicate(self, nums: List[int]) -> int:
    fast = slow = 0
    # proves that we have a cycle
    while True:
      fast = nums[nums[fast]]
      slow = nums[slow]
      if fast == slow: break
    
    # find where the cycle is (by resetting both to 1x speed)
    slow2 = 0
    while True:
      slow2 = nums[slow2]
      slow = nums[slow]
      if slow == slow2: return slow