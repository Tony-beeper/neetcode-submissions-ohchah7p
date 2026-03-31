class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        n = len(grid)
        m = len(grid[0])

        q = deque()

        for i in range(n):
            for j in range(m):
                if grid[i][j] == 2:
                    q.append((0,i,j))
        minute = 0
        dirs = [(-1,0),(1,0),(0,-1), (0,1)]
        while q:
            time, r, c = q.popleft()
            for x,y in dirs:
                nr, nc = r + x, c + y
                if nr >= n or nr < 0 or nc >= m or nc <0:
                    continue
                if grid[nr][nc] == 2 or grid[nr][nc] == 0:
                    continue
                grid[nr][nc] = 2
                q.append((time+1, nr,nc))
                minute = time + 1
        for i in range(n):
            for j in range(m):
                if grid[i][j] == 1:
                    return -1
        return minute

