class Solution:
    # Time: O(n)
    # Space: O(1)
    def maxProfit(self, prices: List[int]) -> int:
        max_profit = 0
        min_price = float('inf')
        for i in range(len(prices)):
            if prices[i] <= min_price:
                min_price = prices[i]
            
            if prices[i] > min_price:
                x = (prices[i] - min_price)
                if x > max_profit:
                    max_profit = x
        
        return max_profit
    


    def maxProfit2(self, prices: List[int]) -> int:
        max_profit = 0
        min_price = float('inf')

        for price in prices:
            if price < min_price:
                min_price = price
            
            profit = price - min_price 

            if profit > max_profit: 
                max_profit = profit
            
        return max_profit
    
            