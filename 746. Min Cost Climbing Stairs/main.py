class Solution:
    def minCostClimbingStairs(cost: list[int]) -> int:
        n = len(cost)
        dp = [0] * n
        dp[0], dp[1] = cost[0], cost[1]
        
        for i in range(2, n):
            dp[i] = cost[i] + min(dp[i-1], dp[i-2])
            print("dp", dp[i])
            print("cost", cost[i])
            
        print(dp[-1], dp[-2])
        return min(dp[-1], dp[-2])
    
    print(minCostClimbingStairs([1,100,1,1,1,100,1,1,100,1]))