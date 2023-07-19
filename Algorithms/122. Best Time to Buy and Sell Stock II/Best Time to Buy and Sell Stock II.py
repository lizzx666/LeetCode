'''
You are given an array prices where prices[i] is the price of a given stock on the ith day.

Find the maximum profit you can achieve. You may complete as many transactions as you like (i.e., buy one and sell one share of the stock multiple times).

Note: You may not engage in multiple transactions simultaneously (i.e., you must sell the stock before you buy again).

 

Example 1:

Input: prices = [7,1,5,3,6,4]
Output: 7
Explanation: Buy on day 2 (price = 1) and sell on day 3 (price = 5), profit = 5-1 = 4.
Then buy on day 4 (price = 3) and sell on day 5 (price = 6), profit = 6-3 = 3.
Example 2:

Input: prices = [1,2,3,4,5]
Output: 4
Explanation: Buy on day 1 (price = 1) and sell on day 5 (price = 5), profit = 5-1 = 4.
Note that you cannot buy on day 1, buy on day 2 and sell them later, as you are engaging multiple transactions at the same time. You must sell before buying again.
Example 3:

Input: prices = [7,6,4,3,1]
Output: 0
Explanation: In this case, no transaction is done, i.e., max profit = 0.

'''

class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        dp = [[0 for i in range(2)] for j in range(len(prices))]
        #dp[i][0]:record the largest value if hold stock on day i
        #dp[i][1]:record the largest value if don't hold stock on day i        
        dp[0][0] = -prices[0]
        dp[0][1] = 0

        for i in range(1,len(prices)):
            dp[i][0] = max(dp[i-1][0],dp[i-1][1]-prices[i])
            dp[i][1] = max(dp[i-1][1],dp[i-1][0]+prices[i])
        
        return dp[-1][1]

class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        result = 0
        for i in range(1,len(prices)):
            result += max(0,prices[i]-prices[i-1])
        return result

def maxProfit(prices):
    max_profit = 0
    for i in range(1,len(prices)):
        if prices[i]>prices[i-1]:
            max_profit += prices[i]-prices[i-1]
    return max_profit
