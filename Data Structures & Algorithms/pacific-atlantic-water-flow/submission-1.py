class Solution:
    def pacificAtlantic(self, heights: List[List[int]]) -> List[List[int]]:
        n = len(heights)
        m = len(heights[0])
        pacific = set()
        atlantic = set()

        dirs = [(1,0),(-1,0), (0,-1), (0,1)]
        def dfs(i,j, visited):
            if (i,j) in visited:
                return
            
            visited.add((i,j))

            for x,y in dirs:
                nr, nc = x + i, y + j
                if nr >= n or nr < 0 or nc >= m or nc < 0:
                    continue
                if (nr,nc) in visited or heights[nr][nc] < heights[i][j]:
                    continue
                dfs(nr,nc,visited)
        
        for i in range(m):
            dfs(0,i, pacific)
        for i in range(n):
            dfs(i,0, pacific)

        for i in range(m):
            dfs(n-1,i, atlantic)
        for i in range(n):
            dfs(i,m-1, atlantic)

        res = []
        for i in range(n):
            for j in range(m):
                if (i,j) in atlantic and (i,j) in pacific:
                    res.append([i,j])

        return res
