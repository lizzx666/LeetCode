'''
Given an m x n binary matrix filled with 0's and 1's, find the largest square containing only 1's and return its area.

 

Example 1:
Input: matrix = [["1","0","1","0","0"],["1","0","1","1","1"],["1","1","1","1","1"],["1","0","0","1","0"]]
Output: 4

Example 2:
Input: matrix = [["0","1"],["1","0"]]
Output: 1

Example 3:
Input: matrix = [["0"]]
Output: 0

'''

#dp
class Solution:
    def maximalSquare(self, matrix: List[List[str]]) -> int:
        m = len(matrix)
        n = len(matrix[0])
        if m == 0 or n==0:
            return 0 
        #dp = [[0 for _ in range(n+1)] for _ in range(m+1)]
        dp = [[0]* (n+1) for _ in range(m+1)]

        max_side = 0
        for i in range(1,m+1):
            for j in range(1,n+1):
                if matrix[i-1][j-1]=='1':
                    if i==1 or j==1:
                        dp[i][j] = 1
                    else:
                        dp[i][j] = min(dp[i-1][j-1],dp[i][j-1],dp[i-1][j])+1
                    max_side = max(max_side,dp[i][j])
            
        return max_side*max_side


#also dp
class Solution:
    def maximalSquare(self, matrix: List[List[str]]) -> int:
        m = len(matrix)
        n = len(matrix[0])
        if m == 0 or n==0:
            return 0 
        dp = [[0 for _ in range(n)] for _ in range(m)]
        #dp = [[0]*n for _ in range(m)] (correct)
        #dp = [[0]*n]*m] (incorrect, cannot write like this)
        max_side = 0
        for i in range(m):
            for j in range(n):
                if matrix[i][j]=='1':
                    if i==0 or j==0:
                        dp[i][j] = 1
                    else:
                        dp[i][j] = min(dp[i-1][j-1],dp[i][j-1],dp[i-1][j])+1
                    max_side = max(max_side,dp[i][j])
            
        return max_side*max_side
