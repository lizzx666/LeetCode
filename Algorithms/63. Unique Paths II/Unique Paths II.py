'''

A robot is located at the top-left corner of a m x n grid (marked 'Start' in the diagram below).

The robot can only move either down or right at any point in time. 
The robot is trying to reach the bottom-right corner of the grid (marked 'Finish' in the diagram below).

Now consider if some obstacles are added to the grids. How many unique paths would there be?

An obstacle and space is marked as 1 and 0 respectively in the grid.


Example 1:
Input: obstacleGrid = [[0,0,0],[0,1,0],[0,0,0]]
Output: 2
Explanation: There is one obstacle in the middle of the 3x3 grid above.
There are two ways to reach the bottom-right corner:
1. Right -> Right -> Down -> Down
2. Down -> Down -> Right -> Right


Example 2:
Input: obstacleGrid = [[0,1],[0,0]]
Output: 1

'''


class Solution:
    def uniquePathsWithObstacles(self, obstacleGrid: List[List[int]]) -> int:
        m = len(obstacleGrid)
        n = len(obstacleGrid[0])

        if obstacleGrid[0][0]!=0 or obstacleGrid[m-1][n-1]!=0:
            return 0


        dp = [[0 for _ in range(n)] for _ in range(m)]

        i = 0
        j = 0

        while i <= m-1 and obstacleGrid[i][0]==0:
            dp[i][0]=1
            i+=1
        while j <= n-1 and obstacleGrid[0][j]==0:
            dp[0][j]=1
            j+=1
        #print(dp)
        for i in range(1,m):
            for j in range(1,n):
                if obstacleGrid[i][j] == 0:
                    dp[i][j] = dp[i-1][j] + dp[i][j-1]

        return dp[m-1][n-1]
    
    

class Solution:
    def uniquePathsWithObstacles(self, obstacleGrid: List[List[int]]) -> int:
        m = len(obstacleGrid)
        n = len(obstacleGrid[0])
        if obstacleGrid[0][0]==1:
            return 0
        obstacleGrid[0][0]=1
        for i in range(1,m):
            if obstacleGrid[i][0]==1:
                obstacleGrid[i][0]=0
            else: 
                obstacleGrid[i][0]=obstacleGrid[i-1][0]
        for j in range(1,n):
            if obstacleGrid[0][j]==1:
                obstacleGrid[0][j]=0
            else:
                obstacleGrid[0][j]=obstacleGrid[0][j-1]
        for i in range(1,m):
            for j in range(1,n):
                if obstacleGrid[i][j]==0:
                    obstacleGrid[i][j] = obstacleGrid[i-1][j] + obstacleGrid[i][j-1]
                else:
                    obstacleGrid[i][j]=0
        return obstacleGrid[m-1][n-1]
