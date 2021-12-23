'''
Given an n x n binary matrix grid, return the length of the shortest clear path in the matrix. If there is no clear path, return -1.

A clear path in a binary matrix is a path from the top-left cell (i.e., (0, 0)) to the bottom-right cell (i.e., (n - 1, n - 1)) such that:

All the visited cells of the path are 0.
All the adjacent cells of the path are 8-directionally connected (i.e., they are different and they share an edge or a corner).
The length of a clear path is the number of visited cells of this path.

 

Example 1
Input: grid = [[0,1],[1,0]]
Output: 2

Example 2:
Input: grid = [[0,0,0],[1,1,0],[1,1,0]]
Output: 4

Example 3:
Input: grid = [[1,0,0],[1,1,0],[1,1,0]]
Output: -1

'''



class Solution:
    def shortestPathBinaryMatrix(self, grid: List[List[int]]) -> int:
        
        max_row = len(grid) - 1
        max_col = len(grid[0]) - 1
        directions = [(-1,-1),(-1,0),(-1,1),(0,-1),(0,1),(1,-1),(1,0),(1,1)]
        
        def get_neighbors(row,col):
            for i,j in directions:
                new_row = row + i
                new_col = col + j
                if not(0<=new_row <=max_row and 0<=new_col<=max_col):
                    continue
                if grid[new_row][new_col]!=0:
                    continue
                yield (new_row,new_col)
                
        if grid[0][0] != 0 or grid[max_row][max_col] != 0:
            return -1
        
        queue = deque()
        queue.append((0,0))
        grid[0][0] = 1
        
        while queue:
            row,col = queue.popleft()
            distance = grid[row][col]
            if (row,col) == (max_row,max_col):
                return distance
            for neigh_row,neigh_col in get_neighbors(row,col):
                grid[neigh_row][neigh_col] = distance + 1
                queue.append((neigh_row,neigh_col))
        
        return -1
