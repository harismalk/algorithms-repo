class Solution:
    def pacificAtlantic(self, heights: List[List[int]]) -> List[List[int]]:
        ROWS, COLS = len(heights), len(heights[0])
        atl = set()
        pac = set()
        q = deque()
        res = []

        for r in range(ROWS):
            for c in range(COLS):
                if r == 0 or c == 0:
                    pac.add((r,c))
                    q.append([r,c, "pac"])
                elif r == ROWS-1 or c == COLS-1:
                    atl.add((r,c))
                    q.append(([r,c,"atl"]))
        
        while q:
            r,c, ocean = q.popleft
            checkNei(r,c)
            checkNei(r,c)
            checkNei(r,c)
        
            
        

            
            
        