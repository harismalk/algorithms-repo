class Solution:
    def shipWithinDays(self, weights: List[int], d: int) -> int:
        # ship package within d days
        # weights[i] -> weight of ith package
        
        l, r = max(weights), sum(weights)
        res = r

        def canShip(cap):
            days, currCap = 1, cap
            curr = 0
            for w in weights:
                if curr+w > currCap:
                    days+=1
                    if days > d:
                        return False
                    curr = 0
                curr+=w

            return True
        while l <= r:
            cap = (l + r) // 2
            if canShip(cap):
                res = min(res, cap)
                r = cap - 1
            else:
                l = cap + 1

        return res
                
                    
                

            
