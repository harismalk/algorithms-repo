class Solution:
    def checkIfPrerequisite(self, numCourses: int, prerequisites: List[List[int]], queries: List[List[int]]) -> List[bool]:
        adj = {i: [] for i in range(numCourses)}

        for pre, crs in prerequisites:
            adj[crs].append(pre)
        res = []


        def dfs(pre, crs):
            if crs == pre:
                return True
            if adj[crs] == []:
                return False
            for nei in adj[crs]:
                if not dfs(pre, nei):
                    return False
            return True


        for pre, crs in queries:
            res.append(dfs(pre, crs))
        return res

        
    
