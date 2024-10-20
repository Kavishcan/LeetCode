class Solution:
    def uniquePaths(m: int, n: int) -> int:
        dp = [[1] * n for _ in range(m)]
        print(dp)	
        for i in range(1, m):
            for j in range(1, n):
                dp[i][j] = dp[i-1][j] + dp[i][j-1]
                print(dp)
        return dp[-1][-1]
        
    print(uniquePaths(3, 7))