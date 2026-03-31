class Solution:
    def spiralOrder(self, matrix: List[List[int]]) -> List[int]:

        n = len(matrix)
        m = len(matrix[0])
        left = 0
        right = m - 1
        top = 0
        bot = n - 1
        res = []
        while top < bot and left < right:

            for i in range(left, right):
                res.append(matrix[top][i])
            for j in range(top, bot):
                res.append(matrix[j][right])
            for i in range(right, left, -1):
                res.append(matrix[bot][i])
            for j in range(bot, top, -1):
                res.append(matrix[j][left])
            left += 1
            right -= 1
            top += 1
            bot -= 1
        # print(res)
        if top == bot:
            for i in range(left, right+1):
                res.append(matrix[top][i])
        elif left == right:
            for j in range(top, bot+1):
                res.append(matrix[j][right])
        # print(left)
        # print(right)
        # print(top)
        # print(bot)
        return res




