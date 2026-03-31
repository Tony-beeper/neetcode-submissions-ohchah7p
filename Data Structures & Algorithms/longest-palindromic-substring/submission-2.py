class Solution:
    def longestPalindrome(self, s: str) -> str:
        n = len(s)
        dp = [[False] * n for _ in range(n)]
        res = ""
        for i in range(n):
            dp[i][i] = True
            res = s[i]
        
        for length in range(2, n+1):
            for i in range(n-length+1):
                j = i + length -1

                if length == 2:
                    dp[i][j] = s[i] == s[j]
                else:
                    dp[i][j] = s[i] == s[j] and dp[i+1][j-1]
                
                if dp[i][j] and j - i + 1 > len(res):
                    res = s[i:j+1]
                
        return res
                
