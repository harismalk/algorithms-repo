class Solution:
    def climbStairs(self, n: int) -> int:
        #lets say n = 5

        one = two = 1

        for i in range(n-1):
            temp = one + two
            two = one
            one = temp
        return one
        