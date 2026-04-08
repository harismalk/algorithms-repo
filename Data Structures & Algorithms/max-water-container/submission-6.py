class Solution:
    def maxArea(self, heights: List[int]) -> int:

        l = 0
        r = len(heights)-1

        res = 0

        while l < r:

            height = min(heights[r], heights[l])
            width = r - l 

            area = height * width

            res = max(res, area)

            if heights[r] >= heights[l]:
                l+=1
            else:
                r-=1

        return res



            


        