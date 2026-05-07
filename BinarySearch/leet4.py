# Median of Two Sorted Arrays
# Given two sorted arrays nums1 and nums2 of size m and n respectively, return the median of the two sorted arrays.
# The overall run time complexity should be O(log (m+n)).

class Solution:
  def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
    A, B = nums1, nums2
    total = len(nums1) + len(nums2)
    half = total // 2

    if len(B) < len(A):
      A, B = B, A # we want the A to be always smaller

    l, r = 0, len(A) - 1
    while True:
      i = (l + r) // 2 # A
      j = half - i - 2 # B , since arrays are indexed at 0, A starts at 0, B starts at 0, hence we do -2

      Aleft = A[i] if i >= 0 else float("-infinity")
      Aright = A[i + 1] if (i + 1) < len(A) else float("infinity")
      Bleft = B[j] if j >= 0 else float("-infinity")
      Bright = B[j + 1] if (j + 1) < len(B) else float("infinity")

      # partition is correct
      if Aleft <= Bright and Bleft <= Aright:
        # odd
        if total % 2:
          return min(Aright, Bright)
        # even
        return (max(Aleft, Bleft) + min(Aright, Bright)) / 2
      elif Aleft > Bright:
        r = i - 1
      else:
        l = i + 1
