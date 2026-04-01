class Solution:
    def generateMatrix(self, n: int) -> List[List[int]]:
        res = [[0 for _ in range(n)] for _ in range(n)]

        # print(res)
        left = 0
        right = n-1
        cur_num = 1
        while left < right:
            top =left
            bot = right
            for i in range(left, right):
                res[top][i] = cur_num
                cur_num += 1
            for j in range(top, bot):
                res[j][right] = cur_num
                cur_num += 1
            for i in range(right, left, -1):
                res[bot][i] = cur_num
                cur_num += 1
            for j in range(bot, top, -1):
                res[j][left] = cur_num
                cur_num += 1
            left += 1
            right -= 1
        if left == right:
            res[left][right] = cur_num
        return res
