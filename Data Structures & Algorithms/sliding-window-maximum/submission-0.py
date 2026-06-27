class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:

       

        q = deque()

        q.append(nums[0])
        q.append(nums[1])
        res = []
        

        for i in range(2, len(nums)):
            q.append(nums[i])
            res.append(max(q))
            q.popleft()
        return res


            


        