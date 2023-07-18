'''
You are given an array prices where prices[i] is the price of a given stock on the ith day.

You want to maximize your profit by choosing a single day to buy one stock and choosing a different day in the future to sell that stock.

Return the maximum profit you can achieve from this transaction. If you cannot achieve any profit, return 0.

 

Example 1:
Input: prices = [7,1,5,3,6,4]
Output: 5
Explanation: Buy on day 2 (price = 1) and sell on day 5 (price = 6), profit = 6-1 = 5.
Note that buying on day 2 and selling on day 1 is not allowed because you must buy before you sell.

Example 2:
Input: prices = [7,6,4,3,1]
Output: 0
Explanation: In this case, no transactions are done and the max profit = 0.
'''



class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        if len(prices)==1:
            return 0
        
        dp = [[0 for i in range(2)] for j in range(len(prices))]

        #dp[i][0] means on day i, the max value if we hold this stock
        #dp[i][1] means on day i, the max value if we don't hold this stock

        dp[0][0] = -prices[0]
        dp[0][1] = 0

        for i in range(1,len(prices)):
            dp[i][0] = max(dp[i-1][0],-prices[i])
            dp[i][1] = max(dp[i-1][1],dp[i-1][0]+prices[i])

        return dp[-1][1]


class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        min_value = float('inf')
        max_profit = 0
        
        for i in range(len(prices)):
            min_value = min(prices[i],min_value)
            max_profit = max(max_profit,prices[i]-min_value)
            
        return max_profit
       
       

class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        if not prices or len(prices)<=1:
            return 0
        n = len(prices)
        min_value = prices[0]
        curr_profit = float('-inf')
        max_profit = float('-inf')
        
        for i in range(1,n):
            min_value = min(min_value,prices[i])
            curr_profit = prices[i] - min_value
            max_profit = max(max_profit,curr_profit)
            
        return max_profit

       
class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        n = len(prices)
        if n<=1:
            return 0
        dp = [[0]*2 for i in range(n)]
        #cash value of buy stock on day 1(index 0)
        dp[0][0] = -prices[0]
        #cash value of don't buy stock on day 1(index 0)
        dp[0][1] = 0
        for i in range(1,n):
            #cash value of hold or buy stock on day i
            dp[i][0] = max(dp[i-1][0],-prices[i]) 
            #cash value of didn't hold or sell stock
            dp[i][1] = max(dp[i-1][1],dp[i-1][0]+prices[i])
        return dp[-1][1]


class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        min_price = float("inf")
        max_profit = 0
        for i in range(len(prices)):
            if prices[i] < min_price:
                min_price = prices[i]
            elif prices[i] - min_price > max_profit:
                max_profit = prices[i] - min_price
        return max_profit

       
 
