class Twitter:

    def __init__(self):
        self.time = 0
        self.followMap = defaultdict(set)
        self.tweetMap = defaultdict(list)
        

    def postTweet(self, userId: int, tweetId: int) -> None:
        self.tweetMap[userId].append([tweetId, self.time])
        self.time -= 1
        

    def getNewsFeed(self, userId: int) -> List[int]:
        res = []
        maxHeap = []

        self.followMap[userId].add(userId)
        for followeeId in self.followMap[userId]:
            if self.tweetMap[followeeId]:
                index = len(self.tweetMap[followeeId])-1
                tweetId, time = self.tweetMap[followeeId][index]
                maxHeap.append([time, tweetId, followeeId, index-1])
        
        heapq.heapify(maxHeap)

        while len(res) < 10 and maxHeap:
            time, tweetId, followerId, index = heapq.heappop(maxHeap)
            res.append(tweetId)
            if index >= 0:
                tweetId, time = self.tweetMap[followerId][index]
                heapq.heappush(maxHeap, [time, tweetId, followerId, index])

        return res

    def follow(self, followerId: int, followeeId: int) -> None:
        self.followMap[followerId].add(followeeId)
        

    def unfollow(self, followerId: int, followeeId: int) -> None:
        if followeeId in self.followMap[followerId]:
            self.followMap[followerId].remove(followeeId)
        
