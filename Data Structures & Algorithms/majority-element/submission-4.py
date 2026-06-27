class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        count = defaultdict(int)
        res = maxCnt = 0

        for num in nums:
            count[num] +=1
            if maxCnt < count[num]:
                res = num
                maxCount = count[num]
        return res
                