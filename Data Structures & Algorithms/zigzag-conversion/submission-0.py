class Solution:
    def convert(self, s: str, numRows: int) -> str:
        if len(s) <= numRows or numRows == 1:
            return s
        
        rows = [""] * numRows
        cur = 0
        direction = -1

        for ch in s:
            rows[cur] += ch
            if cur == numRows - 1 or cur == 0:
                direction *= -1
            cur += direction
        return "".join(rows)


