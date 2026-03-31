class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        cur_min = float('inf')
        rev = 0
        for p in prices:
            cur_min = min(cur_min, p)
            rev = max(rev, p-cur_min)
        return rev