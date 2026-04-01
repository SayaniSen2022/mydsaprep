# Valid Palindrome
import re

class Solution:
  def isPalindrome(self, s: str) -> bool:
    res = re.sub(r"[^a-zA-Z0-9]", "", s).lower() #replacing all non=alphanumerics
    # two pointers
    left, right = 0, len(res)-1
    while left <= right:
      if res[left] == res[right]:
        left+=1
        right-=1
      else:
        return False
    return True

#Run
if __name__ == "__main__":
    sol = Solution()

    input_string = "A man, a plan, a canal: Panama"

    print(sol.isPalindrome(input_string))