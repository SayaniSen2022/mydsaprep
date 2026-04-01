# Two Sum II - Input Array Is Sorted
# 1-indexed array of integers numbers that is already sorted in ascending order
# Return the indices of the two numbers index1 and index2, each incremented by one, as an integer array [index1, index2]

class Solution:
  def twoSum(self, numbers: List[int], target: int) -> List[int]:
    l, r = 0 , len(numbers)-1
    while l < r:
      currSum = numbers[l] + numbers[r]
      if currSum > target:
        r-=1
      elif currSum < target:
        l+=1
      else:
        return [l+1, r+1]
if __name__ == "__main__":
  sol = Solution()
  print(sol.twoSum([2, 3, 11, 4], 6))