class Solution:
    def solve(self, board: List[List[str]]) -> None:
        n = len(board)
        m = len(board[0])
        visited = set()
        dirs = [(1,0),(-1,0), (0,-1), (0,1)]
        def dfs(i,j,visited):
            if board[i][j] == "X" or (i,j) in visited:
                return
            
            visited.add((i,j))

            for x, y in dirs:
                nr, nc = x+i, j+y
                if nr >= n or nr < 0 or nc >= m or nc <0:
                    continue
                if board[nr][nc] == "X":
                    continue
                dfs(nr,nc, visited)

            

        
        for i in range(n):
            dfs(i,0, visited)
        for j in range(m):
            dfs(0,j, visited)

        
        for i in range(n):
            dfs(i,m-1, visited)
        for j in range(m):
            dfs(n-1,j, visited)



        for i in range(n):
            for j in range(m):
                if (i,j) not in visited:
                    board[i][j] = "X"


