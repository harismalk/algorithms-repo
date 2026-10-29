class Solution:
    def maxArea(self, heights: List[int]) -> int:
        res = 0
        l, r = 0, len(heights)-1

        while l < r:
            length = min(heights[l], heights[r])
            width = r-l
            area = length * width
            res = max(area, res)
            if heights[l] > heights[r]:
                r-=1
            else:
                l+=1
        return res