class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:



        q = deque()
        res = []
        for i in range(k):
            q.append(nums[i])
        

        for i in range(k-1, len(nums)):
            q.append(nums[i])
            res.append(max(q))
            q.popleft()
        return res


            


        