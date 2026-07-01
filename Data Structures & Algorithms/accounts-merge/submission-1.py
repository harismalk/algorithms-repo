class UnionFind:
    def __init__(self, size):
        self.root = [i for i in range(size)]
        self.rank = [0] * size
    def union(self, x, y):
        rootX, rootY = self.find(x), self.find(y)
        if rootX != rootY:
            if self.rank[rootX] > self.rank[rootY]:
                self.root[rootY] = rootX
            elif self.rank[rootY] > self.rank[rootX]:
                self.root[rootX] = rootY
            else:
                self.root[rootY] = rootX
                self.rank[rootX] +=1
    def find(self, x):
        if x == self.root[x]:
            return x
        self.root[x] = self.find(self.root[x])
        return self.root[x]

class Solution:
    def accountsMerge(self, accounts: List[List[str]]) -> List[List[str]]:
        n = len(accounts)
        uf = UnionFind(n)
        emailToAcc = defaultdict(int)

        for i, account in enumerate(accounts):
            for email in account[1:]:
                if email in emailToAcc:
                    uf.union(i, emailToAcc[email])
                else:
                    emailToAcc[email] = i
        

        emailGroups = defaultdict(list)

        for e, acc in emailToAcc.items():
            leader = uf.find(acc)
            emailGroups[leader].append(e)
        
        res = []

        for i, emails in emailGroups.items():
            name = accounts[i][0]
            res.append([name] + sorted(emails))
        return res

        

        
        
            









        