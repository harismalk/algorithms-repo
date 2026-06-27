class Twitter:

    def __init__(self):
        self.time = 0
        self.tweetMap = defaultdict(list)
        self.followMap = defaultdict(set)
        

    def postTweet(self, userId: int, tweetId: int) -> None:
        self.tweetMap[userId].append([tweetId, self.time])
        self.time-=1
        

    def getNewsFeed(self, userId: int) -> List[int]:
        self.followMap[userId].add(userId)
        maxHeap = []
        res = []
        for followeeId in self.followMap[userId]:
            if self.tweetMap[followeeId]:
                index = len(self.tweetMap[followeeId])
                maxHeap.append([-time, tweetId, followeeId, index-1])
            heapq.heapify(maxHeap)
            while len(res)>10 or maxHeap:
                time, tweetId, followeeId, index = heapq.heappop(maxHeap)
                res.append(tweetId)
                if index >=0:
                    time, tweetId = tweetMap[followeeId][index]
                    heapq.heappush(minHeap, [time, tweetId, followeeId, index-1])
            return res


                    


        

    def follow(self, followerId: int, followeeId: int) -> None:
        self.followMap[followerId].add(followeeId)
        

    def unfollow(self, followerId: int, followeeId: int) -> None:
        if followeeId in self.followMap[followerId]:
            self.followMap[followerId].remove(followeeId)

        
