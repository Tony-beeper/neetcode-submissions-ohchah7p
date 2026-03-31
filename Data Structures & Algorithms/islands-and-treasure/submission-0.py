class Solution:
    def islandsAndTreasure(self, grid: List[List[int]]) -> None:
        n = len(grid)
        m = len(grid[0])
        q =deque()
        for i in range(n):
            for j in range(m):
                if grid[i][j] == 0:
                    q.append((i,j))
        dirs = [(1,0),(-1,0), (0,-1), (0,1)]
        while q:
            r, c = q.popleft()

            for x,y in dirs:
                nr,nc = x+r, y + c
                if nr < 0 or nr >= n or nc < 0 or nc >= m:
                    continue
                if grid[nr][nc] != 2147483647:
                    continue
                grid[nr][nc] = grid[r][c] + 1
                q.append((nr,nc))
