class Solution:
    def spiralOrder(self, matrix: List[List[int]]) -> List[int]:
        n = len(matrix)
        m = len(matrix[0])

        left = 0
        top = 0
        right = m - 1
        bot = n - 1
        res = []
        while left < right and top < bot:

            for j in range(left, right):
                res.append(matrix[top][j])
            for i in range(top, bot):
                res.append(matrix[i][right])
            # bot
            for j in range(right, left, -1):
                res.append(matrix[bot][j])
            for i in range(bot, top, -1):
                res.append(matrix[i][left])
            left += 1
            top +=1
            right -=1
            bot -=1
        if left == right:
            # if bot == top:
            #     res.append(matrix[left][right])
            # else:
            for i in range(top, bot+1):
                res.append(matrix[i][right])
        elif bot == top:
            for j in range(left, right+1):
                res.append(matrix[top][j])
        return res
