class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        cur_min = prices[0]

        profit = 0

        for p in prices:
            if p < cur_min:
                cur_min = p
            profit = max(profit, p - cur_min)
        return profit

