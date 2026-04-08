class Solution:
    def maxArea(self, heights: List[int]) -> int:
        res = 0
        l, r = 0, len(heights)-1

        while l<r:
            width = r-l
            length = min(heights[r], heights[l])
            area = length*width
            res = max(res, area)
            if heights[r] > heights[l]:
                l+=1
            else:
                r-=1
        return res
