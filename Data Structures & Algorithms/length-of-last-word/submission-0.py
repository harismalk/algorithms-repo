class Solution:
    def lengthOfLastWord(self, s: str) -> int:
        split = s.split(" ")
        for s in split:
            s.strip()
            
        return len(split[len(split)-1])