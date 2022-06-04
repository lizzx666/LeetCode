'''
Given an m x n matrix board containing 'X' and 'O', capture all regions that are 4-directionally surrounded by 'X'.

A region is captured by flipping all 'O's into 'X's in that surrounded region.

 

Example 1:
Input: board = [["X","X","X","X"],["X","O","O","X"],["X","X","O","X"],["X","O","X","X"]]
Output: [["X","X","X","X"],["X","X","X","X"],["X","X","X","X"],["X","O","X","X"]]
Explanation: Surrounded regions should not be on the border, which means that any 'O' on the border of the board are not flipped to 'X'. 
Any 'O' that is not on the border and it is not connected to an 'O' on the border will be flipped to 'X'. 
Two cells are connected if they are adjacent cells connected horizontally or vertically.


Example 2:
Input: board = [["X"]]
Output: [["X"]]


'''


class Solution:
    def solve(self, board: List[List[str]]) -> None:
        """
        Do not return anything, modify board in-place instead.
        """
        
        if not board or not board[0]:
            return
        
        self.ROWS = len(board)
        self.COLS = len(board[0])
        
        from itertools import product
        
        boarders = list(product(range(self.ROWS),[0,self.COLS-1])) \
                    + list(product([0,self.ROWS-1],range(self.COLS)))
        
                                                                          
        for row,col in boarders:
            self.DFS(board,row,col)
        
        for i in range(self.ROWS):
            for j in range(self.COLS):
                if board[i][j] == 'O': board[i][j]='X'
                elif board[i][j] == 'E': board[i][j] = 'O'
                           
    def DFS(self,board,row,col):
        if row<0 or row>=len(board) or col<0 or col>=len(board[0]) or board[row][col]!='O':
            return
        board[row][col]='E'
        for i,j in [(-1,0),(1,0),(0,-1),(0,1)]:
            self.DFS(board,row+i,col+j)
