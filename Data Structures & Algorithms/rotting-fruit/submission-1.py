class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        n = len(grid)
        m = len(grid[0])
        q = deque()
        ROTTEN = 2
        FRESH = 1
        EMPTY = 0
        # minutes = 0
        dirs = [(0,1), (0,-1), (1,0), (-1,0)]
        for i in range(n):
            for j in range(m):
                if grid[i][j] == ROTTEN:
                    q.append((i,j,0))
        minutes = 0
        while q:
            r, c, minute = q.popleft()

            for i,j in dirs:
                nr, nc = r + i, c + j
                if nr < n and nr >= 0 and nc >= 0 and nc < m:
                    if grid[nr][nc] == FRESH:
                        minutes = minute + 1
                        q.append((nr,nc,minutes))
                        grid[nr][nc] = ROTTEN


        for i in range(n):
            for j in range(m):
                if grid[i][j] == FRESH:
                    return -1


        return minutes



        

