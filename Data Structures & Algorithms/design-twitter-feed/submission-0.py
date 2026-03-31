class Twitter:

    def __init__(self):
        self.tweets = defaultdict(list)
        self.following = defaultdict(set)
        self.timestamp = 0


    def postTweet(self, userId: int, tweetId: int) -> None:
        self.tweets[userId].append((self.timestamp, tweetId))
        self.timestamp -= 1

    def getNewsFeed(self, userId: int) -> List[int]:
        minheap = []
        res = []
        followeelist = self.following[userId] | {userId}
        for u in followeelist:
            if self.tweets[u]:
                # print(self.tweets)
                idx = len(self.tweets[u]) - 1
                time, tweetId = self.tweets[u][idx]
                heapq.heappush(minheap, (time, tweetId, u, idx-1))
        # print(minheap)
        while minheap and len(res) < 10:
            time, tweetId, uid, idx = heapq.heappop(minheap)
            res.append(tweetId)
            if idx >= 0:
                time, tweetId = self.tweets[uid][idx]
                heapq.heappush(minheap, (time, tweetId, uid, idx-1))
        return res


    def follow(self, followerId: int, followeeId: int) -> None:
        self.following[followerId].add(followeeId)

    def unfollow(self, followerId: int, followeeId: int) -> None:
        self.following[followerId].discard(followeeId)
