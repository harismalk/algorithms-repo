class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
        # Map it to a LL
        # no exit conditon in this kind of LL -> cycle must exist
        # Floyds Algo fins beginning of a cycle

        slow = fast = 0
        while True:
            slow = nums[slow]
            fast = nums[nums[fast]]
            if slow == fast:
                break
            
        slow2 = 0
        while True:
            slow = nums[slow]
            slow2 = nums[slow2]
            if slow == slow2:
                return slow





         
        