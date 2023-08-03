'''

The n-queens puzzle is the problem of placing n queens on an n x n chessboard such that no two queens attack each other.

Given an integer n, return all distinct solutions to the n-queens puzzle. You may return the answer in any order.

Each solution contains a distinct board configuration of the n-queens' placement, 
where 'Q' and '.' both indicate a queen and an empty space, respectively.

 

Example 1:
Input: n = 4
Output: [[".Q..","...Q","Q...","..Q."],["..Q.","Q...","...Q",".Q.."]]
Explanation: There exist two distinct solutions to the 4-queens puzzle as shown above


Example 2:
Input: n = 1
Output: [["Q"]]


'''




class Solution:
    def solveNQueens(self, n: int) -> List[List[str]]:
        res = []
        chessboard = ['.' * n for _ in range(n)]
        self.backtracking(chessboard,n,0,res)
        return res

    def backtracking(self,chessboard,n,row,res):
        if row==n:
            res.append(chessboard[:])
            return
        
        for col in range(n):
            if self.isvalid(row,col,chessboard):
                chessboard[row] = chessboard[row][:col]+'Q'+chessboard[row][col+1:]
                #chessboard[row][i]='Q'
                self.backtracking(chessboard,n,row+1,res)
                chessboard[row] = chessboard[row][:col]+'.'+chessboard[row][col+1:]
                #chessboard[row][i]='.'
    
    def isvalid(self,row,col,chessboard):
        #check whether upside have 'Q
        for i in range(row):
            if chessboard[i][col]=='Q':
                return False
        
        #check whether left-up side have 'Q'
        i = row-1
        j = col-1
        while i>=0 and j>=0:
            if chessboard[i][j]=='Q':
                return False
            i-=1
            j-=1
        
        #check whether right-up side have 'Q'
        i = row-1
        j = col+1
        while i>=0 and j<len(chessboard):
            if chessboard[i][j]=='Q':
                return False
            i-=1
            j+=1
        return True
