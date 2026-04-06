class Solution:
    def pacificAtlantic(self, heights: List[List[int]]) -> List[List[int]]:
        pacific = set()
        atlantic = set()
        n = len(heights)
        m = len(heights[0])
        pacific_q = []
        atlantic_q = []
        for i in range(n):
            pacific.add((i,0))
            pacific_q.append((i,0))
        for j in range(m):
            pacific.add((0,j))
            pacific_q.append((0,j))
        for i in range(n):
            atlantic.add((i,m-1))
            atlantic_q.append((i,m-1))
        for j in range(m):
            atlantic.add((n-1,j))
            atlantic_q.append((n-1,j))
        dirs = [(0,1), (1,0), (-1,0), (0,-1)]
        while pacific_q:
            r,c = pacific_q.pop()
            for i,j in dirs:
                nr,nc = i + r, c + j
                if 0<= nr< n and 0<=nc< m and (nr,nc) not in pacific and heights[nr][nc] >= heights[r][c]:
                    pacific.add((nr,nc))
                    pacific_q.append((nr,nc))

        while atlantic_q:
            r,c = atlantic_q.pop()
            for i,j in dirs:
                nr,nc = i + r, c + j
                if 0<= nr< n and 0<=nc< m and (nr,nc) not in atlantic and heights[nr][nc] >= heights[r][c]:
                    atlantic.add((nr,nc))
                    atlantic_q.append((nr,nc))
        res = []
        for i in range(n):
            for j in range(m):
                if (i,j) in pacific and (i,j) in atlantic:
                    res.append((i,j))
        return res

        

