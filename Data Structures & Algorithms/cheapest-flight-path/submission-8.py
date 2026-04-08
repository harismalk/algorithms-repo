class Solution:
    def findCheapestPrice(self, n: int, flights: List[List[int]], src: int, dst: int, k: int) -> int:
        maxStops = k+1
        prices = [float("INF")] * n
        prices[src] = 0

        for stop in range(maxStops):
            tmpPrices = prices.copy()
            for s,d,p in flights:
                if prices[s] == float("INF"):
                    continue
                if prices[s] + p < tmpPrices[d]:
                    tmpPrices[d] = prices[s] + p
            prices = tmpPrices
        
        return -1 if prices[dst] == float("INF") else prices[dst]

        