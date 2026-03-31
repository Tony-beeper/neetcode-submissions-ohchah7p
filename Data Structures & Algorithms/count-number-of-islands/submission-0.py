class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        n = len(grid) # n = rows
        m = len(grid[0]) # m = columns
        count = 0

        def dfs(i,j):
            if grid[i][j] == "1":
                grid[i][j] = "0"
            else:
                return
            for x in range(-1,2):
                for y in range(-1,2):
                    if 0 <= i + x < n and 0 <= j + y < m:
                        dfs(i+x,j)
                        dfs(i,j + y)
            # print(grid)
        for i in range(n):
            for j in range(m):
                if grid[i][j] == "1":
                    count += 1
                    dfs(i,j)
        return count