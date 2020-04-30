class Solution:
    def longestCommonSubsequence(self, text1: str, text2: str) -> int:
        rows = len(text1) + 1
        cols = len(text2) + 1
        dp = [[0 for i in range(cols)] for j in range(rows)]
        print(dp)
        for i in range(1, rows):
            for j in range(1, cols):
                if text1[i - 1] == text2[j - 1]:
                    dp[i][j] = dp[i - 1][j - 1] + 1
                else:
                    dp[i][j] = max(dp[i - 1][j], dp[i][j - 1])
                print(dp)   
        
        return dp[-1][-1]
        
        
A=Solution()
A.longestCommonSubsequence("abcde", "ace")