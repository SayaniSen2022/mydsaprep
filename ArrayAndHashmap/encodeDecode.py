# Design an algorithm to encode a list of strings to a string. The encoded string is then sent over the network and is decoded back to the original list of strings.

from typing import List

class Solution:
  def encode(self, strs: List[str]) -> str:
    res = ""
    for s in strs:
      res += str(len(s)) + "#" + s
    return res
  
  def decode(self, s: str) -> List[str]:
    res, i = [], 0
    while(i < len(s)):
      j = i
      while(s[j] != "#"):
        j += 1
      length = int(s[i : j])
      res.append(s[j+1 : j + 1 + length])
      i = j + 1 + length
    return res
  
#code for running
if  __name__ == "__main__":
  sol = Solution()

  strs = ["neet", "code", "love", "you"]
  encoded = sol.encode(strs)
  print("Encoded:", encoded)

  decoded = sol.decode(encoded)
  print("Decoded:", decoded)
