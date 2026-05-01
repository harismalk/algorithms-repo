class Solution:
    def majorityElement(self, nums: List[int]) -> List[int]:
        freq = Counter(nums)
        length = len(nums)

        return [num for num, cnt in freq.items() if cnt > length/3]
        

        for num, cnt in freq.items():
            if cnt > (length/3):
                res.append(num)
        return res