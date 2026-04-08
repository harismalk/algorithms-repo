class Solution:
    def trap(self, height: List[int]) -> int:
        
        right = len(height)-1
        left = 0
        res = 0
        left_max = height[0]
        right_max = height[len(height)-1]

        while left < right:

            if left_max <= right_max:
                res += left_max - height[left]
                left += 1
                left_max = max(left_max, height[left])
            else:
                res += right_max - height[right]
                right -= 1
                right_max = max(right_max, height[right])
        return res


        
