'''

Given two strings s and t, return the number of distinct subsequences of s which equals t.

The test cases are generated so that the answer fits on a 32-bit signed integer.

 

Example 1:
Input: s = "rabbbit", t = "rabbit"
Output: 3


Example 2:
Input: s = "babgbag", t = "bag"
Output: 5


'''




class Solution:
    def numDistinct(self, s: str, t: str) -> int:
        dp = [[0 for j in range(len(t)+1)] for i in range(len(s)+1)]
        #dp[i][j]: the count of t end at position j-1 in s end at position i-1
        for i in range(len(s)+1):
            #dp[i][0] ->t end with position -1-> t is empty string. s have 1 empty string t
            #dp[0][j] -> s end with position -1->s is empty string. s has 0 chance to include t while t is not empty string
            dp[i][0]=1
        
        for i in range(1,len(s)+1):
            for j in range(1,len(t)+1):
                if s[i-1]==t[j-1]:
                    dp[i][j]=dp[i-1][j-1]+dp[i-1][j]
                else:
                    dp[i][j]=dp[i-1][j]
        return dp[-1][-1]
