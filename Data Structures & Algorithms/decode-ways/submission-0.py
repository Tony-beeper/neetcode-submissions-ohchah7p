class Solution:
    def numDecodings(self, s: str) -> int:
        n = len(s)
        dp = [0] * (n+1)
        print(dp)
        dp[n] = 1 # "" empty string


        for i in range(n-1, -1,-1):
            digit = int(s[i])
            if s[i] != '0':
                dp[i] = dp[i+1]
            else:
                continue
            
            if i + 1 < n:
                if 10 <= int(s[i:i+2]) <=26:
                    dp[i] += dp[i+2]
        return dp[0]

            

