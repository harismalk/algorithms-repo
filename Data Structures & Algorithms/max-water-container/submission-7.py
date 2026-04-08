class Solution:
    def maxArea(self, heights: List[int]) -> int:

        r = len(heights)-1
        l = 0
        res = 0

        while r > l:

            height = min(heights[l], heights[r])
            width = r - l
            area = height * width

            res = max(res,area)

            if heights[r] < heights[l]:
                r-=1
            else:
                l+=1
        return res

        