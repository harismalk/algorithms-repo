class Solution:
    def canCompleteCircuit(self, gas: List[int], cost: List[int]) -> int:
        if sum(gas) < sum(cost):
            return -1
        
        tank = gas[0]
        res = 0

        for i in range(1, len(gas)):
            tank-=cost[i-1]
            if tank < 0:
                res = i
                tank  = 0
            tank += gas[i]
        return res if tank >= 0 else -1


            