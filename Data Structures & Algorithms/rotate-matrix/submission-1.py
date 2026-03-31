class Solution:
    def rotate(self, matrix: List[List[int]]) -> None:
        # (0,1) -> (1,2)
        # (1,2) -> (2,1)
        # (2,1) -> (1,0)
        # (1,0) -> (0,1)
        # [1,4,7]
        # [2,5,8]
        # [3,6,9]
        n = len(matrix)
        for i in range(n):
            for j in range(i+1, n):
                matrix[i][j], matrix[j][i] = matrix[j][i], matrix[i][j]
        
        for row in matrix:
            row.reverse()
