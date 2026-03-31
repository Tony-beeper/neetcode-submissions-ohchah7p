class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        n = len(nums)
        max_val = -float('inf')
        dp = [[1] * (n) for _ in range(n)]
        print(dp)
        for i in range(n):
            dp[i][i] = nums[i]
            max_val = max(dp[i][i], max_val)
        for length in range(2,len(nums)+1):
            for i in range(n - length + 1):
                j = i + length - 1
                dp[i][j] = dp[i][j-1] * nums[j]
                # print(dp)
                max_val = max(dp[i][j], max_val)
        print(dp)
        return max_val
