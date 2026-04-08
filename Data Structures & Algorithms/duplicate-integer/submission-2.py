class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        seen = set()  # Corrected variable name from 'processed' to 'seen'
        for num in nums:  # Ensure consistent variable name 'num'
            if num in seen:
                return True
            seen.add(num)
        return False  # Properly aligned with the 'for' loop
