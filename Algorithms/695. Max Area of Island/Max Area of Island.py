'''

You are given an m x n binary matrix grid. 
An island is a group of 1's (representing land) connected 4-directionally (horizontal or vertical.) 
You may assume all four edges of the grid are surrounded by water.

The area of an island is the number of cells with a value 1 in the island.

Return the maximum area of an island in grid. If there is no island, return 0.

 

Example 1:
Input: grid = [[0,0,1,0,0,0,0,1,0,0,0,0,0],[0,0,0,0,0,0,0,1,1,1,0,0,0],[0,1,1,0,1,0,0,0,0,0,0,0,0],[0,1,0,0,1,1,0,0,1,0,1,0,0],[0,1,0,0,1,1,0,0,1,1,1,0,0],[0,0,0,0,0,0,0,0,0,0,1,0,0],[0,0,0,0,0,0,0,1,1,1,0,0,0],[0,0,0,0,0,0,0,1,1,0,0,0,0]]
Output: 6
Explanation: The answer is not 11, because the island must be connected 4-directionally.


Example 2:
Input: grid = [[0,0,0,0,0,0,0,0]]
Output: 0

'''



class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        m = len(grid)
        n = len(grid[0])
        max_area = 0
        for i in range(m):
            for j in range(n):
                if grid[i][j]==1:
                    max_area = max(self.dfs(grid,i,j),max_area)
        return max_area
        
    def dfs(self,grid,i,j):
        if i < 0 or i >= len(grid) or j < 0 or j >= len(grid[0]) or grid[i][j]!=1:
            return 0
        
        grid[i][j] = 0  
        area = 1
        for di, dj in [[-1,0],[1,0],[0,-1],[0,1]]:
            next_i,next_j = i+di,j+dj
            area += self.dfs(grid,next_i,next_j)

        return area
