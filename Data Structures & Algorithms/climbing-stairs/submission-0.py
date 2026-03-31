class Solution:
    def climbStairs(self, n: int) -> int:
        if n == 1:
            return 1

        elif n == 2:
            return 2

        arr = [1,2]

        for i in range(2, n):
            cur = arr[i-1] +arr[i-2]
            arr.append(cur)
        return arr[-1]