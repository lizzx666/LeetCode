'''
Given an integer rowIndex, return the rowIndexth (0-indexed) row of the Pascal's triangle.

In Pascal's triangle, each number is the sum of the two numbers directly above it as shown:

Example 1:
Input: rowIndex = 3
Output: [1,3,3,1]

Example 2:
Input: rowIndex = 0
Output: [1]

Example 3:
Input: rowIndex = 1
Output: [1,1]

'''


class Solution:
    def getRow(self, rowIndex: int) -> List[int]:
        row = [1]
        for _ in range(0,rowIndex):
            row = [x+y for x,y in zip([0]+row , row+[0])]
        return row
    
    
    
    
    
class Solution:
    def getRow(self, rowIndex: int) -> List[int]:
        dp = [[1]* (i+1) for i in range(rowIndex+1)]

        for i in range(2,rowIndex+1):
            for j in range(1,i):
                dp[i][j] = dp[i-1][j-1] + dp[i-1][j]
                
        return dp[rowIndex]
