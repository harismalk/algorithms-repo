class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        res = []
        q = deque()
        l, r = 0,0

        while r < len(nums):
            while q and q[0] < nums[r]:
                q.pop()
            q.append(r)

            if l > q[-1]:
                q.popleft()
            
            if (r+1) >= k:
                res.append(q[-1])
                l+=1
            r+=1
        return res

