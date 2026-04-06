class Solution:
    def islandsAndTreasure(self, grid: List[List[int]]) -> None:
        n = len(grid)
        m = len(grid[0])
        dirs = [(0,1), (1,0), (0,-1), (-1,0)]
        LAND = 2147483647
        TREASURE = 0
        WATER = -1
        q = []
        
        for i in range(n):
            for j in range(m):
                if grid[i][j] == TREASURE:
                    q.append((i,j))
        visited = [[False for _ in range(m)] for _ in range(n)]
        # print(q)
        while q:
            r,c = q.pop(0)
            visited[r][c] = True
            for x,y in dirs:
                nr, nc = x+r, y +c
                if 0<=nr< n and 0 <= nc < m and grid[nr][nc] != TREASURE and grid[nr][nc] != WATER and visited[nr][nc] != True:
                    if grid[nr][nc] == LAND:
                        grid[nr][nc] = grid[r][c] + 1
                    visited[nr][nc] = True
                    q.append((nr,nc))
                    # print('hi')






