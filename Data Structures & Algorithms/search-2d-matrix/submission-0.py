class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        res = []

        for m in matrix:
            res += m

        left = 0
        right = len(res) - 1

        while left <= right:
            mid_index = int((left + right) / 2)
            mid = res[mid_index]
            if mid > target:
                right = mid_index - 1
            elif mid < target:
                left = mid_index + 1
            else:
                return True
        return False