'''


Write a program to solve a Sudoku puzzle by filling the empty cells.

A sudoku solution must satisfy all of the following rules:

Each of the digits 1-9 must occur exactly once in each row.
Each of the digits 1-9 must occur exactly once in each column.
Each of the digits 1-9 must occur exactly once in each of the 9 3x3 sub-boxes of the grid.
The '.' character indicates empty cells.

 

Example 1:
Input: board = [["5","3",".",".","7",".",".",".","."],
["6",".",".","1","9","5",".",".","."],
[".","9","8",".",".",".",".","6","."],
["8",".",".",".","6",".",".",".","3"],
["4",".",".","8",".","3",".",".","1"],
["7",".",".",".","2",".",".",".","6"],
[".","6",".",".",".",".","2","8","."],
[".",".",".","4","1","9",".",".","5"],
[".",".",".",".","8",".",".","7","9"]]

Output: [["5","3","4","6","7","8","9","1","2"],
["6","7","2","1","9","5","3","4","8"],
["1","9","8","3","4","2","5","6","7"],
["8","5","9","7","6","1","4","2","3"],
["4","2","6","8","5","3","7","9","1"],
["7","1","3","9","2","4","8","5","6"],
["9","6","1","5","3","7","2","8","4"],
["2","8","7","4","1","9","6","3","5"],
["3","4","5","2","8","6","1","7","9"]]
Explanation: The input board is shown above and the only valid solution is shown below:




'''





class Solution:
    def solveSudoku(self, board: List[List[str]]) -> None:
        """
        Do not return anything, modify board in-place instead.
        """
        self.backtracking(board)
    def backtracking(self,board):
        for i in range(len(board)):
            for j in range(len(board)):
                if board[i][j]!='.':
                    continue
                for k in range(1,10):
                    if self.is_valid(i,j,k,board):
                        board[i][j]=str(k)
                        if self.backtracking(board):
                            return True
                        board[i][j]='.'
                return False
        return True

    def is_valid(self,row,col,val,board):
        #check whether contrdict in the same row
        for j in range(9):
            if board[row][j]==str(val):
                return False
        
        #check whether contradict in the same col
        for i in range(9):
            if board[i][col]==str(val):
                return False
        
        #check whether contradict in the small zone
        start_row = (row//3)*3
        start_col = (col//3)*3
        for i in range(start_row,start_row+3):
            for j in range(start_col,start_col+3):
                if board[i][j]==str(val):
                    return False
        
        return True
