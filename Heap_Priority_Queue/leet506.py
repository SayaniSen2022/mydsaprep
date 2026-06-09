# Relative Ranks: You are given an integer array score of size n, where score[i] is the score of the ith athlete in a competition. 
# All the scores are guaranteed to be unique. The athletes are placed based on their scores, where the 1st place athlete has the highest score, the 2nd place athlete has the 2nd highest score, and so on. The placement of each athlete determines their rank:
# The 1st place athlete's rank is "Gold Medal".
# The 2nd place athlete's rank is "Silver Medal".
# The 3rd place athlete's rank is "Bronze Medal".
# For the 4th place to the nth place athlete, their rank is their placement number (i.e., the xth place athlete's rank is "x").
# Return an array answer of size n where answer[i] is the rank of the ith athlete.
# Input: score = [10,3,8,9,4]
# Output: ["Gold Medal","5","Bronze Medal","Silver Medal","4"]

from typing import List
import heapq

class Solution:
  def findRelativeRanks(self, score: List[int]) -> List[str]:
    max_heap = [(-s, i) for i, s in enumerate(score)] # negating the value since python does not have in-built max-heap
    heapq.heapify(max_heap) # produces a max-heap: [-10, -9, -8, -4, -3]
    # print(score)

    answer = [""] * len(score) # pre-allocate with correct size
    rank = 1

    while max_heap:
      val, idx = heapq.heappop(max_heap) # pops highest score first
      # print(val, idx)
      if rank == 1:
        answer[idx] = "Gold Medal"
      elif rank == 2:
        answer[idx] = "Silver Medal"
      elif rank == 3:
        answer[idx] = "Bronze Medal"
      else:
        answer[idx] = str(rank)
      rank += 1
    return answer



if __name__ == "__main__":
  score = [10,3,8,9,4]
  sol = Solution()
  result = sol.findRelativeRanks(score)
  print(result)