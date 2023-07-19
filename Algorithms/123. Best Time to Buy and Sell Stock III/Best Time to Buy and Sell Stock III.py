'''
You are given an array prices where prices[i] is the price of a given stock on the ith day.

Find the maximum profit you can achieve. You may complete at most two transactions.

Note: You may not engage in multiple transactions simultaneously (i.e., you must sell the stock before you buy again).

 

Example 1:
Input: prices = [3,3,5,0,0,3,1,4]
Output: 6
Explanation: Buy on day 4 (price = 0) and sell on day 6 (price = 3), profit = 3-0 = 3.
Then buy on day 7 (price = 1) and sell on day 8 (price = 4), profit = 4-1 = 3.

Example 2:
Input: prices = [1,2,3,4,5]
Output: 4
Explanation: Buy on day 1 (price = 1) and sell on day 5 (price = 5), profit = 5-1 = 4.
Note that you cannot buy on day 1, buy on day 2 and sell them later, as you are engaging multiple transactions at the same time. You must sell before buying again.

Example 3:
Input: prices = [7,6,4,3,1]
Output: 0
Explanation: In this case, no transaction is done, i.e. max profit = 0.

Example 4:
Input: prices = [1]
Output: 0
'''


class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        dp = [[0 for i in range(4)] for j in range(len(prices))]

        #dp[i][0]:first hold
        #dp[i][1]:first unhold
        #dp[i][2]:second hold
        #dp[i][3]:second unhold

        dp[0][0]=-prices[0]
        dp[0][1]=0
        dp[0][2]=-prices[0]
        dp[0][3]=0

        for i in range(1,len(prices)):
            dp[i][0] = max(dp[i-1][0],-prices[i])
            dp[i][1] = max(dp[i-1][1],dp[i-1][0]+prices[i])
            dp[i][2] = max(dp[i-1][2],dp[i-1][1]-prices[i])
            dp[i][3] = max(dp[i-1][3],dp[i-1][2]+prices[i])

        return max(dp[-1][1],dp[-1][3])

def maxProfit(prices):
    t1_buy, t2_buy = -float('inf'),-float('inf')
    t1_sell, t2_sell = 0,0
    for price in prices:
        t1_buy = max(t1_buy,-price)
        t1_sell = max(t1_sell, price+t1_buy)
        t2_buy = max(t2_buy,t1_sell-price)
        t2_sell = max(t2_sell,price+t2_buy)
    return t2_sell
