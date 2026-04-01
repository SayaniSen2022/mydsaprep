# Leet 128. Longest Consecutive Sequence
# Given an unsorted array of integers nums, return the length of the longest consecutive elements sequence.
# You must write an algorithm that runs in O(n) time.

class Solution:
  def longestConsecutiveSequence(self, nums: List[int]) -> int:
    numsSet = set(nums)
    longest = 0
    
    for n in nums:
      #checking if its the beginning of a sequence
      if (n - 1) in numsSet:
        length = 0
        while (n + length):
          length += 1
          longest = max(length, longest)
      return longest