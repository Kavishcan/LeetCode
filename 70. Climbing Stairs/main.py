class Solution:
    def climbStairs(n: int) -> int:
        if n == 1:
            return 1
        if n == 2:
            return 2
        
        first = 1
        second = 2
        for i in range(3, n+1):
            second, first = first + second, second
        
        return second
    
    print(climbStairs(7))