# Task Scheduler: You are given an array of CPU tasks, each labeled with a letter from A to Z, and a number n. 
# Each CPU interval can be idle or allow the completion of one task. Tasks can be completed in any order, 
# but there's a constraint: there has to be a gap of at least n intervals between two tasks with the same label.
# Return the minimum number of CPU intervals required to complete all tasks.
from typing import List
from collections import Counter, deque
import heapq

class Solution:
  def leastInterval(self, tasks: List[str], n: int) -> int:
    count = Counter(tasks)
    max_heap = [-cnt for cnt in count.values()]
    heapq.heapify(max_heap)

    time = 0
    q = deque() # pairs of [-cnt, idleTime]
    while max_heap or q:
      time += 1
      if max_heap:
        cnt = 1 + heapq.heappop(max_heap)
        if cnt:
          q.append([cnt, time + n])
      if q and q[0][1] == time:
        heapq.heappush(max_heap, q.popleft()[0])
    return time
