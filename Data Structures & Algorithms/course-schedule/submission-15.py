class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        preMap = {i: [] for i in range(numCourses)}

        for crs, pre in prerequisites:
            preMap[crs].append(pre)
        
        visited = set()

        def dfs(i):
            if i in visited:
                return False
            if preMap[i] == []:
                return True
            visited.add(i)

            for pre in preMap[i]:
                if not dfs(pre):
                    return False
            visited.remove(i)
            preMap[i] = []
            return True
        
        for crs in range(numCourses):
            if not dfs(crs):
                return False
        return True