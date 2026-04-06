class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        n = len(grid)
        m = len(grid[0])

        visited = [[False for _ in range(m)] for _ in range(n)]
        dirs = [(0,1), (1,0), (0,-1), (-1,0)]
        num_island = 0
        for i in range(n):
            for j in range(m):
                if grid[i][j] == "1" and not visited[i][j]:
                    q = [(i,j)]
                    visited[i][j] = True
                    num_island += 1
                    while q:
                        r,c = q.pop(0)
                        for x,y in dirs:
                            nr, nc = r+x, c+y
                            if 0<=nr<n and 0<=nc < m and grid[nr][nc] == "1" and not visited[nr][nc]:
                                visited[nr][nc] = True
                                q.append((nr,nc))
        return num_island
