'''
You are given an integer array prices where prices[i] is the price of a given stock on the ith day, and an integer k.

Find the maximum profit you can achieve. You may complete at most k transactions.

Note: You may not engage in multiple transactions simultaneously (i.e., you must sell the stock before you buy again).

 

Example 1:

Input: k = 2, prices = [2,4,1]
Output: 2
Explanation: Buy on day 1 (price = 2) and sell on day 2 (price = 4), profit = 4-2 = 2.

Example 2:
Input: k = 2, prices = [3,2,6,5,0,3]
Output: 7
Explanation: Buy on day 2 (price = 2) and sell on day 3 (price = 6), profit = 6-2 = 4. Then buy on day 5 (price = 0) and sell on day 6 (price = 3), profit = 3-0 = 3.
'''


class Solution:
    def maxProfit(self, k: int, prices: List[int]) -> int:
        n = len(prices)
        profit = 0
        if not prices or k==0:
            return 0
        elif 2*k>n:
            for i in range(1,n): 
                if prices[i]>prices[i-1]:
                    profit += prices[i]-prices[i-1]
            return profit
        else:
            buy_arr = [-float('inf')]*(k+1)
            sell_arr = [0]*(k+1)
            for price in prices:
                for i in range(1,k+1):
                    buy_arr[i] = max(buy_arr[i],sell_arr[i-1]-price)
                    sell_arr[i] = max(sell_arr[i],buy_arr[i]+price)
            return sell_arr[k]
