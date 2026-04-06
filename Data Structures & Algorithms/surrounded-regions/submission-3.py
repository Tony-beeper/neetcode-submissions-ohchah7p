class Solution:
    def solve(self, board: List[List[str]]) -> None:
        safe = set()

        n = len(board)
        m = len(board[0])

        for i in range(n):
            if board[i][0] == "O":
                safe.add((i,0))
            if board[i][m-1] == "O":
                safe.add((i,m-1))
        for j in range(m):
            if board[0][j] == "O":
                safe.add((0,j))
            if board[n-1][j] == "O":
                safe.add((n-1,j))
        safe_q = [(i,j) for i,j in safe]
        dirs = [(0,1), (1,0), (-1,0), (0,-1)]
        while safe_q:
            r, c = safe_q.pop(0)
            for i,j in dirs:
                nr,nc = i+r, c+j
                if 0<= nr < n and 0<= nc < m and (nr,nc) not in safe and board[nr][nc] == "O":
                    safe.add((nr,nc))
                    safe_q.append((nr,nc))
        for i in range(n):
            for j in range(m):
                if (i,j) not in safe:
                    board[i][j] = "X"

            

