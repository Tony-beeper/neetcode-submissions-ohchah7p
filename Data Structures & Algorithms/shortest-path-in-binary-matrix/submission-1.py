class Solution:
    def shortestPathBinaryMatrix(self, grid: List[List[int]]) -> int:
        n = len(grid)
        m = len(grid[0])
        if grid[0][0] == 1 or grid[n-1][m-1] == 1:
            return -1

        dirs = [(0,1),(1,0),(-1,0),(0,-1),(1,1),(-1,-1),(-1,1),(1,-1)]
        grid_dis = [[float('inf') for _ in range(m)] for _ in range(n)]
        grid_dis[0][0] = 1
        # def dfs(i,j):
        #     if i == n - 1 and j == m - 1 and grid[i][j] == 0:
        #         return 1
        #     if grid_dis[i][j] != float('inf'):

        q = deque()
        q.append((0,0))
        visited = set()
        visited.add((0,0))
        while q:
            r, c = q.popleft()
            # visited.add((r,c))
            for i,j in dirs:
                nr, nc = i+r, c+j
                if 0 <= nr < n and 0 <= nc < m and grid[nr][nc] == 0:
                    grid_dis[nr][nc] = min(grid_dis[nr][nc], grid_dis[r][c] + 1)
                    if (nr,nc) not in visited:
                        q.append((nr,nc))
                        visited.add((nr,nc))
        return grid_dis[n-1][m-1] if grid_dis[n-1][m-1]!=float('inf') else -1
            
                    



            
            


        return dfs(0,0)