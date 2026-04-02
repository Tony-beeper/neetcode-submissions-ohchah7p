class UnionFind:
    def __init__(self,n):
        self.rank = [1 for _ in range(n)]
        self.parent = [i for i in range(n)] # own parents
    
    def find(self,x):
        # path compression
        while x != self.parent[x]:
            self.parent[x] = self.parent[self.parent[x]]
            x = self.parent[x]
        return x

    def union(self,a,b):
        a = self.find(a)
        b = self.find(b)
        rank_a = self.rank[a]
        rank_b = self.rank[b]

        if rank_a > rank_b:
            self.rank[a] += rank_b
            self.parent[b] = a
        else:
            self.rank[b] += rank_a
            self.parent[a] = b
        


class Solution:
    def accountsMerge(self, accounts: List[List[str]]) -> List[List[str]]:
        size = len(accounts)
        uf = UnionFind(size)

        emails = {}
        
        for i, account in enumerate(accounts):
            name  = account[0]
            for email in account[1:]:
                if emails.get(email) != None:
                    # if i == 4:
                        # print("hi")
                        # print(emails[email])
                    uf.union(i, emails[email])
                emails[email] = i
        # print(emails)
        # print(uf.parent)
        idxToEmails = defaultdict(list)
        for email, idx in emails.items():
            idx = uf.find(idx)

            idxToEmails[idx].append(email)

        res = []
        print(uf.parent)
        for idx, email in idxToEmails.items():
            email.sort()
            name = accounts[idx][0]
            res.append([name] + email)
        return res














