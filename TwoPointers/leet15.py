# 3sum: Given an integer array nums, return all the triplets [nums[i], nums[j], nums[k]] such that i != j, i != k, and j != k, and nums[i] + nums[j] + nums[k] == 0. 
# Notice that the solution set must not contain duplicate triplets.

class Solution:
  def threeSum(self, nums: list[int]) -> list[list[int]]:
    res = []
    nums.sort()

    for i, a in enumerate(nums):
      if i > 0 and a == nums[i-1]: # checking for duplicates
        continue

      # two sum II
      l, r = i+1, len(nums)-1
      while l < r:
        three_sum = a + nums[l] + nums[r]
        if three_sum > 0:
          r-=1
        elif three_sum < 0:
          l+=1
        else:
          res.append([a, nums[l], nums[r]])
          # shifting one pointer does the job
          l+=1
          # checking if its the same value for removing duplictes
          while nums[l] == nums[l-1] and l < r:
            continue
    return res
