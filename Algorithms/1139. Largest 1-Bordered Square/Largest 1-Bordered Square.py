'''
Given a 2D grid of 0s and 1s, 
return the number of elements in the largest square subgrid that has all 1s on its border, 
or 0 if such a subgrid doesn't exist in the grid.

 

Example 1:
Input: grid = [[1,1,1],[1,0,1],[1,1,1]]
Output: 9

Example 2:
Input: grid = [[1,1,0,0]]
Output: 1

'''


class Solution:
    def largest1BorderedSquare(self, grid: List[List[int]]) -> int:
        m = len(grid)
        n = len(grid[0])
        dp = [[[0 for _ in range(2)] for _ in range(n+1)] for _ in range(m+1)]
        
        #dp[i][j][0]: counts of continuous 1 for (i,j) per row wise
        #dp[i][j][1]: counts of continuous 1 for (i,j) per col wise
        for i in range(1,m+1):
            for j in range(1,n+1):
                if grid[i-1][j-1]==0:
                    continue
                dp[i][j][0] = dp[i][j-1][0] + 1
                dp[i][j][1] = dp[i-1][j][1] + 1
        
        max_side = 0
        for i in range(1,m+1):
            for j in range(1,n+1):
                #use min of bottom side and right side to decide the possible current side
                cur_side = min(dp[i][j][0],dp[i][j][1])
                #if current side already smaller than max_side per consider from right and bottom
                #then no need to check from upper and left side as not possible to be bigger than max_side
                if cur_side <= max_side:
                    continue
                    
                while cur_side > max_side:
                    #left side and right side
                    #use bottom left's col length and top right's row length to compare with cur_side
                    if dp[i][j-cur_side+1][1] >= cur_side and dp[i-cur_side+1][j][0] >= cur_side:
                        max_side = cur_side
                        break
                    else:
                        cur_side -= 1
        return max_side*max_side
