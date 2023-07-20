'''

Given two strings word1 and word2, return the minimum number of steps required to make word1 and word2 the same.

In one step, you can delete exactly one character in either string.

 

Example 1:
Input: word1 = "sea", word2 = "eat"
Output: 2
Explanation: You need one step to make "sea" to "ea" and another step to make "eat" to "ea".

Example 2:
Input: word1 = "leetcode", word2 = "etco"
Output: 4



'''


class Solution:
    def minDistance(self, word1: str, word2: str) -> int:
        dp=[[0 for j in range(len(word2)+1)] for i in range(len(word1)+1)]
        #dp[i][j]: min operation of making word1 end with i-1 equal to word2 end with j-1 to be the same
        for i in range(len(word1)+1):
            dp[i][0]=i
        
        for j in range(len(word2)+1):
            dp[0][j]=j
        
        for i in range(1,len(word1)+1):
            for j in range(1,len(word2)+1):
                if word1[i-1]==word2[j-1]:
                    dp[i][j]=dp[i-1][j-1]
                else:
                    dp[i][j]=min(dp[i-1][j]+1,dp[i][j-1]+1,dp[i-1][j-1]+2)
        return dp[-1][-1]
