class Solution:
    def ladderLength(self, beginWord: str, endWord: str, wordList: List[str]) -> int:
        if endWord not in wordList or beginWord == endWord:
            return 0
        
        adj = defaultdict(list)
        wordList.append(beginWord)
        res = 1

        for word in wordList:
            for i in range(len(word)):
                pattern = word[:i] + "*" + word[i+1:]
                adj[pattern].append(word)       

        
        visit = set([beginWord])
        q = deque([beginWord])

        while q:
            for _ in range(len(q)):
                w = q.popleft()
                if w == endWord:
                    return res
                
                for i in range(len(w)):
                    pat = w[:i] + "*" + w[i+1:]
                    for nei in adj[pat]:
                        if nei not in visit:
                            q.append(nei)
                            visit.add(nei)
            res+=1

        return 0