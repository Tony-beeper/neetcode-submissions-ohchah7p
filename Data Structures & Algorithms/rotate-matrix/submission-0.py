class Solution:
    def rotate(self, matrix: List[List[int]]) -> None:
        # (0,1) -> (1,2)
        # (1,2) -> (2,1)
        # (2,1) -> (1,0)
        # (1,0) -> (0,1)
        # [1,4,7]
        # [2,5,8]
        # [3,6,9]

        l, r = 0, len(matrix) - 1

        while l < r:
            for i in range(r-l):
                # print(i)
                topleft = matrix[l][l+i]

                # botleft to top left
                matrix[l][l+i] = matrix[r-i][l]

                # botright to botleft
                matrix[r-i][l] = matrix[r][r-i]

                # topright to botright
                matrix[r][r-i] = matrix[l+i][r]

                # topleft to topright
                matrix[l+i][r] = topleft

            l+=1
            r -=1


