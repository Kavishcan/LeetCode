class Solution:
    fib_nums = [
        0, 1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89, 144, 233, 377, 610, 987, 1597, 2584, 4181,
        6765, 10946, 17711, 28657, 46368, 75025, 121393, 196418, 317811, 514229, 832040,
        1346269, 2178309, 3524578, 5702887, 9227465, 14930352, 24157817, 39088169, 63245986,
        102334155, 165580141, 267914296, 433494437, 701408733, 1134903170, 1836311903
    ]

    def fib(self, n):
        return self.fib_nums[n]
    
    def fib2(self, n):
        if n == 0:
            return 0
        if n == 1:
            return 1

        return self.fib2(n - 2) + self.fib2(n - 1)
    

    # Using memoization
    def fib3(self, n):
        memo = {0:0, 1:1}

        def helper(x):
            if x in memo:
                return memo[x]
            else:
                memo[x] = helper(x - 1) + helper(x - 2)
                return memo[x]
            
        return helper(n)
    
    # Using bottom-up approach - tabulation
    def fib4(n):
        if n == 0:
            return 0
        if n == 1:
            return 1

        dp = [0] * (n + 1)
        dp[1] = 1

        for i in range(2, n + 1):
            dp[i] = dp[i - 1] + dp[i - 2]
            print(dp)
        
        return dp[n]
    
    # Using bottom-up approach - tabulation
    def fib5(n):
        if n == 0:
            return 0
        if n == 1:
            return 1

        prev = 0
        cur = 1

        for i in range(2, n + 1):
            prev , cur = cur, prev + cur
        
        return cur
    
    print(fib4(10))