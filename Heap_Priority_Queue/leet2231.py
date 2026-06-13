# Largest Number After Digit Swaps by Parity: You are given a positive integer num. You may swap any two digits of num that have the same parity 
# (i.e. both odd digits or both even digits). Return the largest possible value of num after any number of swaps.

import heapq

class Solution:
  def largestInteger(self, num: int) -> int:
    num_str = list(str(num))
    # print(num_str)
    even = []
    odd = []
    res = []
    even_index, odd_index = 0, 0

    for chr in num_str:
      digit = int(chr)
      if digit % 2 == 0:
        even.append(digit)
      else:
        odd.append(digit)
    # sort in reverse order so that the larger numbers are first
    even.sort(reverse=True)
    odd.sort(reverse=True)

    for d in num_str:
      if int(d) % 2 == 0:
        res.append(str(even[even_index]))
        even_index += 1
      else:
        res.append(str(odd[odd_index]))
        odd_index += 1
    return int("".join(res))





if __name__ == "__main__":
  sol = Solution()
  num = 1234
  result = sol.largestInteger(num)
  print(result)
