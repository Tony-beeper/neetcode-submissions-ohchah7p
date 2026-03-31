class UnionFind:
    def __init__(self,n):
        self.rank = [1] * n
        self.parent = [i for i in range(n)]

    def find(self,i):
        while i != self.parent[i]:
            self.parent[i] = self.parent[self.parent[i]]
            i = self.parent[i]
        return i
    
    def union(self,a,b):
        a_par, b_par = self.find(a), self.find(b)

        if a_par == b_par:
            return
        elif self.rank[a_par] > self.rank[b_par]:
            self.rank[a_par] += self.rank[b_par]
            self.parent[b_par] = a_par
        else:
            self.rank[b_par] += self.rank[a_par]
            self.parent[a_par] = b_par
        




class Solution:
    def accountsMerge(self, accounts: List[List[str]]) -> List[List[str]]:
        emailToAccount = {}
        uf = UnionFind(len(accounts))
        for i, person  in enumerate(accounts):
            for email in person[1:]:
                if emailToAccount.get(email) != None:
                    uf.union(emailToAccount[email], i)
                else:
                    emailToAccount[email] = i
        groupedEmails = defaultdict(list)

        for email, idx in emailToAccount.items():
            leader = uf.find(idx)
            groupedEmails[leader].append(email)
            print(str(leader) + "    "+ str(email))
        res = []
        for idx, emails in groupedEmails.items():
            name = accounts[idx][0]
            res.append([name] + sorted(emails))

        return res


            









            