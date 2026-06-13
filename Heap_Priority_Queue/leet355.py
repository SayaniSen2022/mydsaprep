"""
Design Twitter: Design a simplified version of Twitter where users can post tweets, follow/unfollow another user, 
and is able to see the 10 most recent tweets in the user's news feed.

Implement the Twitter class:

1. Twitter() Initializes your twitter object.

2. void postTweet(int userId, int tweetId) Composes a new tweet with ID tweetId by the user userId. 
Each call to this function will be made with a unique tweetId.

3. List<Integer> getNewsFeed(int userId) Retrieves the 10 most recent tweet IDs in the user's news feed. 
Each item in the news feed must be posted by users who the user followed or by the user themself. 
Tweets must be ordered from most recent to least recent.

4. void follow(int followerId, int followeeId) The user with ID followerId started following the user with ID followeeId.

5. void unfollow(int followerId, int followeeId) The user with ID followerId started unfollowing the user with ID followeeId.

"""

from typing import List
from collections import defaultdict
import heapq

class Twitter:
  def __init__(self):
    self.count = 0 # maintaining the number of tweets, which was created earlier
    self.tweet_map = defaultdict(list) # userId -> list of [count, tweetIds]
    self.follow_map = defaultdict(set) # userId -> set of followeeId
      

  def postTweet(self, userId: int, tweetId: int) -> None:
    self.tweet_map[userId].append([self.count, tweetId])
    self.count -= 1
      

  def getNewsFeed(self, userId: int) -> List[int]:
    res = [] # ordered starting from the most recent tweets
    minHeap = []

    self.follow_map[userId].add(userId)
    for followeeId in self.follow_map[userId]:
      if followeeId in self.tweet_map:
        index = len(self.tweet_map[followeeId]) - 1
        count, tweetId = self.tweet_map[followeeId][index]
        minHeap.append([count, tweetId, followeeId, index - 1])
    heapq.heapify(minHeap)
    while minHeap and len(res) < 10:
      count, tweetId, followeeId, index = heapq.heappop(minHeap)
      res.append(tweetId)

      if index >= 0:
        count, tweetId = self.tweet_map[followeeId][index]
        heapq.heappush(minHeap, [count, tweetId, followeeId, index - 1])
    return res


  def follow(self, followerId: int, followeeId: int) -> None:
    self.follow_map[followerId].add(followeeId)
      

  def unfollow(self, followerId: int, followeeId: int) -> None:
    if followeeId in self.follow_map[followerId]:
      self.follow_map[followerId].remove(followeeId)