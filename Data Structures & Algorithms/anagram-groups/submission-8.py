class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        groups = defaultdict(list)

        for s in strs:
            index = [0] * 26
            for c in s:
                index[ord(c)-ord('a')]+=1
            groups[tuple(index)].append(s)
        
        return list(groups.values())