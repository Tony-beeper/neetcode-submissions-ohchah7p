class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        n = len(grid)
        m = len(grid[0]) 

        max_size = 0
        def dfs(i,j):
            if i >= n or i < 0 or j >= m or j < 0 or grid[i][j] == 0:
                return 0
            grid[i][j] = 0
            count = 1
            count += dfs(i+1,j)
            count += dfs(i-1,j)
            count += dfs(i,j+1)
            count += dfs(i,j-1)
            
            
            return count

        
        for i in range(n):
            for j in range(m):
                if grid[i][j] == 1:
                    max_size = max(max_size,dfs(i,j))
        # print(grid)
        return max_size
        