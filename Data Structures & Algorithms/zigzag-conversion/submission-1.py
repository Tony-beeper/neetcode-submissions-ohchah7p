class Solution:
    def convert(self, s: str, numRows: int) -> str:
        if numRows >= len(s) or numRows == 1:
            return s
        
        rows = ["" for _ in range(numRows)] 
        direction = -1
        cur = 0
        for ch in s:
            rows[cur] += ch
            if cur == 0 or cur == numRows - 1:
                direction *= -1
            cur += direction
        return "".join(rows)


