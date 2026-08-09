class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        groups = defaultdict(list)

        for s in strs:
            cnt = [0] * 26
            for char in s:
                index = ord(char)-ord('a')
                cnt[index]+=1
            groups[tuple(cnt)].append(s)
        
        return list(groups.values())