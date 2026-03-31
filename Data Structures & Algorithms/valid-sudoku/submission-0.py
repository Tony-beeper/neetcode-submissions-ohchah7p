class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        # row
        for i in range(len(board)):
            count_box = [0] * 9
            for j in range(len(board)):
                if board[i][j] == ".":
                    continue
                digit = int(board[i][j])
                count_box[digit-1] += 1
            if max(count_box) > 1:
                return False
        # column
        for i in range(len(board)):
            count_box = [0] * 9
            for j in range(len(board)):
                if board[j][i] == ".":
                    continue
                digit = int(board[j][i])
                count_box[digit-1] += 1
            if max(count_box) > 1:
                return False

        # box
        for i in range(3):
            for j in range(3):
                start_x = i * 3
                start_y = j * 3
                count_box = [0] * 9
                for x in range(start_x, start_x+3):
                    for y in range(start_y, start_y + 3):
                        if board[x][y] == ".":
                            continue
                        digit = int(board[x][y])
                        count_box[digit-1] += 1
                if max(count_box) > 1:
                    return False
        return True
        

            