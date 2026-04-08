class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        cycle = set()
        visited = set()
        preMap = {i: [] for i in range(numCourses)}
        res = []

        for crs, pre in prerequisites:
            preMap[crs].append(pre)
        
        def dfs(crs):
            if crs in cycle:
                return False
            if crs in visited:
                return True
            cycle.add(crs)
            for pre in preMap[crs]:
                if not dfs(pre):
                    return False
            cycle.remove(crs)
            visited.add(crs)
            res.append(crs)
            return True
        
        for c in range(numCourses):
            if not dfs(c):
                return []
        return res
                


        