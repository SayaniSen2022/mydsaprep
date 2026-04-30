# Koko Eating Bananas: Koko loves to eat bananas. There are n piles of bananas, the ith pile has piles[i] bananas. 
# The guards have gone and will come back in h hours.Koko can decide her bananas-per-hour eating speed of k.
# Each hour, she chooses some pile of bananas and eats k bananas from that pile. If the pile has less than k bananas, 
# she eats all of them instead and will not eat any more bananas during this hour.
# Koko likes to eat slowly but still wants to finish eating all the bananas before the guards return.
# Return the minimum integer k such that she can eat all the bananas within h hours.
# Note: h will always be >= len(piles). 
# Example: in a piles[] = [3,4,5,11], k can be in the rang [1,2,3,...,11]. 
# So we do binary search on this possible range of k and and test 
# whether with that particular k koko is able to eat all the bananas in <= h (given). Then we return the min k.

import math

class Solution:
  def minEatingSpeed(self, piles: List[int], h: int) -> int:
    l, r = 1, max(piles) # the left pointer is min k = 1, and right pointer is max no of bananas in a pile in piles array
    
    # we are initialising right pointer it to max of piles 
    # because that is the max speed at which one can eat the bananas and here we are trying to find the min
    res = r 

    while l <= r:
      k = (l + r) // 2
      hours = 0 # we gotta find it
      for p in piles:
        hours += math.ceil(p / k) # calculating how long it takes to finish the pile with current k
      if hours <= h:
        res = min(res, k) # we are updating the k
        # since we were able to finish the bananas in less than h hours, we will keep looking for lower k, therefore r = k - 1
        r = k - 1
      else:
        l = k + 1
    return res
