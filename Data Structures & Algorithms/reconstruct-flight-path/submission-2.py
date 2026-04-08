class Solution:
    def findItinerary(self, tickets: List[List[str]]) -> List[str]:
        tickets.sort()
        adj = {src: [] for src, dest in tickets}

        for src, dest in tickets:
            adj[src].append(dest)
        
        res = ["JFK"]

        def dfs(src):
            if len(res) == len(tickets)+1:
                return True
            if src not in adj:
                return False
            
            temp = list(adj[src])
            for i, nei in enumerate(temp):
                adj[src].pop(i)
                res.append(nei)

                if dfs(nei): return True

                adj[src].insert(i, nei)
                res.pop()
            return False

        dfs("JFK")
        return res
        