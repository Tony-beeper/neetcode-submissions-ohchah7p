class Solution:
    def generateMatrix(self, n: int) -> List[List[int]]:
        left = 0
        right = n - 1

        top = 0
        bot = n - 1

        matrix = [[0 for _ in range(n)] for _ in range(n)]
        counter = 1
        while left < right:
            
            for col in range(left, right):
                matrix[top][col] = counter
                counter += 1
            for row in range(top, bot):
                matrix[row][right] = counter
                counter += 1
            for col in range(right, left, -1):
                matrix[bot][col] = counter
                counter += 1
            for row in range(bot, top, -1):
                matrix[row][left] = counter
                counter += 1 

            left += 1
            top+=1
            right -=1
            bot -=1
        # print(left)
        # print(right)
        if left == right:
            matrix[left][right] = counter
            # print("debug")
        return matrix
