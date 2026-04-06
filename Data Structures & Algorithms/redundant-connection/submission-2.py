class UnionFind:
    def __init__(self, size):
        self.rank = [1 for _ in range(size)]
        self.parent = {}
        for i in range(1, size+1):
            self.parent[i] = i

    def find(self,x):
        while x != self.parent[x]:
            self.parent[x] = self.parent[self.parent[x]]
            x = self.parent[x]
        return x

    def union(self,a,b):
        pa = self.find(a)
        pb = self.find(b)
        a_rank = self.rank[pa-1]
        b_rank = self.rank[pb-1]
        if a_rank > b_rank:
            self.parent[pb] = pa
            self.rank[pa-1] += b_rank
        else:
            self.parent[pa] = pb
            self.rank[pb-1] += a_rank


class Solution:
    def findRedundantConnection(self, edges: List[List[int]]) -> List[int]:
        # return [3,4]
        res = None
        uf = UnionFind(len(edges))
        for i,j in edges:
            par_i = uf.find(i)
            par_j = uf.find(j)
            if par_i == par_j:
                return [i,j]
            uf.union(i,j)
        return None



