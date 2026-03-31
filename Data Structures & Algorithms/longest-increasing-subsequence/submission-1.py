class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:
        n = len(nums)
        dp = [1] * n

        for end in range(n):
            cur_max = 1
            for i in range(end):
                if nums[i] < nums[end]:
                    cur_max = max(cur_max, dp[i]+1)
                    dp[end] = cur_max
                    # print("hi")
        # print(dp)
        return max(dp)