'''

Given a string s, return the number of palindromic substrings in it.

A string is a palindrome when it reads the same backward as forward.

A substring is a contiguous sequence of characters within the string.

 

Example 1:
Input: s = "abc"
Output: 3
Explanation: Three palindromic strings: "a", "b", "c".

Example 2:
Input: s = "aaa"
Output: 6
Explanation: Six palindromic strings: "a", "a", "a", "aa", "aa", "aaa".

'''



class Solution:
    def countSubstrings(self, s: str) -> int:
        dp = [[0 for i in range(len(s))] for j in range(len(s))]
        #dp[i][j]: whether the s start with i and end at j is a palindrome
        res = 0
        for i in range(len(s)-1,-1,-1):
            for j in range(i,len(s)):
                if s[i]==s[j]:
                    if j-i<=1:
                        dp[i][j]=1
                        res+=1
                    else:
                        if dp[i+1][j-1]:
                            dp[i][j]=1
                            res+=1
        return res
