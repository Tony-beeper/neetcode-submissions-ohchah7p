class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        n = len(grid)
        m = len(grid[0])

        visited = [[False for _ in range(m)] for _ in range(n)]
        # print(visited)
        counter = 0
        WATER = "0"
        LAND = "1"
        dirs = [(0,1),(1,0), (-1,0), (0,-1)]
        for i in range(n):
            for j in range(m):
                # print(grid[i][j])
                if grid[i][j] == LAND and not visited[i][j]:
                    # print("debug")
                    counter += 1
                    q = deque()
                    q.append((i,j))
                    visited[i][j] = True
                    while q:
                        a,b = q.popleft()
                        for x, y in dirs:
                            nr = x+a
                            nc = b + y
                            if nr >= 0 and nc >= 0 and nr < n and nc < m:
                                if grid[nr][nc] == LAND and not visited[nr][nc]:
                                    q.append((nr,nc))
                                    visited[nr][nc] = True
        # print(visited)
        return counter
        










