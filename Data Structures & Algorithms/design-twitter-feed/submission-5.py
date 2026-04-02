import heapq
class Twitter:

    def __init__(self):
        self.followers = defaultdict(set)
        self.tweets = defaultdict(list)
        self.time = 0

    def postTweet(self, userId: int, tweetId: int) -> None:
        self.tweets[userId].append((tweetId, self.time))
        self.time -= 1

    def getNewsFeed(self, userId: int) -> List[int]:
        minheap = []

        following = self.followers[userId] | {userId}

        for user in following:
            # append tweets, the latest, from each user
            # with the head being the time
            tweets = self.tweets[user]
            if tweets:
                idx = len(tweets) - 1
                tweet, time = tweets[idx]
                heapq.heappush(minheap,(time, tweet, user, idx))
        counter = 0
        res = []
        while minheap and len(res) < 10:
            time,tweet,user,idx = heapq.heappop(minheap)
            res.append(tweet)
            idx -= 1
            if idx >= 0:
                tweet,time = self.tweets[user][idx]
                heapq.heappush(minheap, (time,tweet,user,idx))
        return res

    def follow(self, followerId: int, followeeId: int) -> None:
        # if followeeId not in self.followers[followerId]:
        self.followers[followerId].add(followeeId)

    def unfollow(self, followerId: int, followeeId: int) -> None:
        # if followeeId in self.followers[followerId]:
        self.followers[followerId].discard(followeeId)





        
