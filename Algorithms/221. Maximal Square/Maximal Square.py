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



class Solution:
    def maximalSquare(self, matrix: List[List[str]]) -> int:
        m = len(matrix)
        n = len(matrix[0])
        if m == 0 or n==0:
            return 0 
        dp = [[0]*n for _ in range(m)]
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
