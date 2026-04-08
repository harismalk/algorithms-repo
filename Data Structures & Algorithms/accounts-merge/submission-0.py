class UnionFind:
    def __init__(self, size):
        self.root = [i for i in range(size)]
        self.rank = [1] * size

    def find(self, x):
        if self.root[x] == x:
            return x
        self.root[x] = self.find(self.root[x])
        return self.root[x]

    def union(self, x, y):
        rootX, rootY = self.find(x), self.find(y)
        if rootX != rootY:
            if self.rank[rootX] > self.rank[rootY]:
                self.root[rootY] = rootX
            elif self.rank[rootY] > self.rank[rootX]:
                self.root[rootX] = rootY
            else:
                self.root[rootY] = rootX
                self.rank[rootX]+=1

    def isConnected(sef, x, y):
        return self.find(x) == self.find(y)

class Solution:
    def accountsMerge(self, accounts: List[List[str]]) -> List[List[str]]:
        # accounts[i] -> [name, email1, email2, email3....]
        # merge accounts with a common email
        # res = [
        #   [[name ,emails.....]
        #]

        uf = UnionFind(len(accounts))
        emailToAcc = {}  # email -> index of acc

        for i, account in enumerate(accounts):
            for email in account[1:]:
                if email in emailToAcc:
                     uf.union(emailToAcc[email], i)
                else:
                    emailToAcc[email] = i
        emailGroups = defaultdict(list)
        
        for email, i in emailToAcc.items():
            leader = uf.find(i)
            emailGroups[leader].append(email)

        res = []

        for i, emails in emailGroups.items():
            name = accounts[i][0]
            res.append([name] + sorted(emailGroups[i]))
        return res


        

        

        



