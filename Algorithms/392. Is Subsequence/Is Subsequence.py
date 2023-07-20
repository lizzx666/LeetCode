'''

Given two strings s and t, return true if s is a subsequence of t, or false otherwise.

A subsequence of a string is a new string that is formed from the original string by deleting some (can be none) of the characters without disturbing the relative positions of the remaining characters. 
(i.e., "ace" is a subsequence of "abcde" while "aec" is not).

 

Example 1:
Input: s = "abc", t = "ahbgdc"
Output: true

Example 2:
Input: s = "axc", t = "ahbgdc"
Output: false


'''


class Solution:
    def isSubsequence(self, s: str, t: str) -> bool:
        dp = [[0 for j in range(len(t)+1)] for i in range(len(s)+1)]
        #dp[i][j]: the max overlap length of s end at [i-1] and t end at [j-1]

        for i in range(1,len(s)+1):
            for j in range(1,len(t)+1):
                if s[i-1]==t[j-1]:
                    dp[i][j]=dp[i-1][j-1]+1
                else:
                    dp[i][j]=dp[i][j-1]
        return True if dp[-1][-1]==len(s) else False
