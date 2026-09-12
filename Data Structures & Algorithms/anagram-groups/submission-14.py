class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        groups = defaultdict(list)

        for s in strs:
            group = [0] * 26
            for char in s:
                index = ord(char)-ord('a')
                group[index]+=1
            groups[tuple(group)].append(s)
        
        return list(groups.values())

