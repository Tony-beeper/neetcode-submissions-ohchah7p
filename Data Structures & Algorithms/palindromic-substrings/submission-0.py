class Solution:
    def countSubstrings(self, s: str) -> int:
        n = len(s)
        dp = [[False] * n for _ in range(n)]
        res = s[0]
        counter = 0
        for i in range(n):
            dp[i][i] = True
            counter +=1
            # res = s[i]
        
        for length in range(2, n+1):
            for i in range(n-length+1):
                j = i + length -1

                if length == 2:
                    dp[i][j] = s[i] == s[j]
                else:
                    dp[i][j] = s[i] == s[j] and dp[i+1][j-1]
                
                if dp[i][j]:
                    counter+=1 
                    if j - i + 1 > len(res):
                        res = s[i:j+1]
                
        return counter
                
        