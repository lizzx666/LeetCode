'''


You are given an array prices where prices[i] is the price of a given stock on the ith day.

Find the maximum profit you can achieve. You may complete as many transactions as you like (i.e., buy one and sell one share of the stock multiple times) with the following restrictions:

After you sell your stock, you cannot buy stock on the next day (i.e., cooldown one day).
Note: You may not engage in multiple transactions simultaneously (i.e., you must sell the stock before you buy again).

 

Example 1:
Input: prices = [1,2,3,0,2]
Output: 3
Explanation: transactions = [buy, sell, cooldown, buy, sell]

Example 2:
Input: prices = [1]
Output: 0


'''



class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        dp = [[0 for i in range(4)] for j in range(len(prices))]
        #dp[i][0]:on day i, hold stock
        #dp[i][1]:on day i, no stock and non-freeze period
        #dp[i][2]:on day i, sell stock
        #dp[i][3]:day i is freeze period

        dp[0][0]=-prices[0]
        dp[0][1]=0
        dp[0][2]=0
        dp[0][3]=0

        for i in range(1,len(prices)):
            dp[i][0] = max(dp[i-1][0],dp[i-1][1]-prices[i],dp[i-1][3]-prices[i])
            dp[i][1] = max(dp[i-1][1],dp[i-1][3])
            dp[i][2] = dp[i-1][0]+prices[i]
            dp[i][3] = dp[i-1][2]
        
        max_val = max(dp[-1][1],dp[-1][2],dp[-1][3])
        return max_val
