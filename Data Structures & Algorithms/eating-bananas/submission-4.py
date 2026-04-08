class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        l, r = 1, max(piles)
        res = r

        while l <= r:
            m = (l+r)//2
            totalTime = 0
            for p in piles:
                totalTime += math.ceil(float(p)/m)
            
            if totalTime <= h:
                r = m - 1
                res = m
            else:
                l = m + 1
        return res
        

        #set left pointer to minimum value, right to maximum value
        #computer the middle value, check if valid (totalTime <= h)
        #if valid -> check if a lower value works
        #if not -> check if a greater value works
         
                



            

        