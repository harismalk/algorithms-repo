class Solution:
    def foreignDictionary(self, words: List[str]) -> str:
        adj = {c: set() for w in words for c in w}
        indegree = {c: 0 for c in adj}

        for i in range(len(words)-1):
            word1, word2 = words[i], words[i+1]
            minLen = min(len(word1), len(word2))
            if word1[:minLen] == word2[:minLen] and len(word1) > len(word2):
                return ""
            for j in range(minLen):
                if word1[j] != word2[j]:
                    if word2[j] not in adj[word1[j]]:
                        adj[word1[j]].add(word2[j])
                        indegree[word2[j]]+=1
                    break
        q = deque([c for c in indegree if indegree[c] == 0])
        res = []

        while q:
            char = q.popleft()
            res.append(char)
            for nei in adj[char]:
                indegree[nei]-=1
                if indegree[nei] == 0:
                    q.append(nei)
        if len(res) != len(indegree):
            return ""
        return "".join(res)





        