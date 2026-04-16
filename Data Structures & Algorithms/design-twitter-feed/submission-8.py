class Twitter:

    def __init__(self):
        self.following = defaultdict(set)
        self.tweets = defaultdict(list)
        self.time = 0


        

    def postTweet(self, userId: int, tweetId: int) -> None:
        self.tweets[userId].append((self.time, tweetId))
        self.time -= 1

        

    def getNewsFeed(self, userId: int) -> List[int]:
        following = self.following[userId] | {userId}
        q = []
        for user in following:
            tweets = self.tweets.get(user)
            if tweets:
                idx = len(tweets) - 1
                time, tweetId = tweets[idx]
                heapq.heappush(q,(time, tweetId, user, idx))
        res = []
        while q and len(res) < 10:
            time, tweetId, user, idx = heapq.heappop(q)
            res.append(tweetId)
            if idx > 0:
                tweets = self.tweets.get(user)
                idx -= 1
                time, tweetId = tweets[idx]
                heapq.heappush(q,(time, tweetId, user, idx))
        return res

        

    def follow(self, followerId: int, followeeId: int) -> None:
        self.following[followerId].add(followeeId)

    def unfollow(self, followerId: int, followeeId: int) -> None:
        # self.following[followeeId].append(followerId)
        self.following[followerId].discard(followeeId)
        
