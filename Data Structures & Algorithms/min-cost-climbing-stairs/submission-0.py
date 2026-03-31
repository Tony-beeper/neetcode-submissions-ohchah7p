class Solution:
    def minCostClimbingStairs(self, cost: List[int]) -> int:
        if len(cost) == 2:
            return cost[0]

        spent = [0,0]
        for i in range(2, len(cost)+1):
            cur = min(spent[i-1] +cost[i-1],spent[i-2]+cost[i-2])
            spent.append(cur)
        return spent[-1]