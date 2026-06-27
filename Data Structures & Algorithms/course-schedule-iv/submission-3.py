class Solution:
    def checkIfPrerequisite(self, numCourses: int, prerequisites: List[List[int]], queries: List[List[int]]) -> List[bool]:
        adj = {i: [] for i in range(numCourses)}

        for pre, crs in prerequisites:
            adj[pre].append(crs)

        res = []


        def dfs(pre, crs):
            if pre == crs:
                return True
            for nei in adj[pre]:
                if dfs(nei, crs):
                    return True
            return False

        for pre, crs in queries:
            res.append(dfs(pre, crs))
        return res

        
    
