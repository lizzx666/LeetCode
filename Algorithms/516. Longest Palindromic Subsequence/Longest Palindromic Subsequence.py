'''
Given a string s, find the longest palindromic subsequence's length in s.

A subsequence is a sequence that can be derived from another sequence by deleting some or no elements without changing the order of the remaining elements.

 

Example 1:
Input: s = "bbbab"
Output: 4
Explanation: One possible longest palindromic subsequence is "bbbb".

Example 2:
Input: s = "cbbd"
Output: 2
Explanation: One possible longest palindromic subsequence is "bb".


'''



class Solution:
    def longestPalindromeSubseq(self, s: str) -> int:
        dp=[[0 for j in range(len(s))] for i in range(len(s))]
        #dp[i][j]:the length of longest palindromuc sequence of s start at i and end at j

        for i in range(len(s)):
            dp[i][i]=1
        
        for i in range(len(s)-1,-1,-1):
            for j in range(i+1,len(s)):
                if s[i]==s[j]:
                    dp[i][j]=dp[i+1][j-1]+2
                else:
                    dp[i][j]=max(dp[i][j-1],dp[i+1][j])

        return dp[0][-1]
