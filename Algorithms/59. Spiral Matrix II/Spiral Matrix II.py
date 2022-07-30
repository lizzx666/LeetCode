'''
Given a positive integer n, generate an n x n matrix filled with elements from 1 to n2 in spiral order.

 

Example 1:
Input: n = 3
Output: [[1,2,3],[8,9,4],[7,6,5]]

Example 2:
Input: n = 1
Output: [[1]]

'''




class Solution:
    def generateMatrix(self, n: int) -> List[List[int]]:
        nums = [[0]*n for _ in range(n)]
        startx, starty = 0,0
        cnt = 1
        mid = n//2
        for offset in range(1,n//2+1):
            #from left to righ
            for j in range(starty,n-offset):
                nums[startx][j]=cnt
                cnt+=1
            #from top to bottom
            for i in range(startx,n-offset):
                nums[i][n-offset]=cnt
                cnt+=1
            #from right to left
            for j in range(n-offset,starty,-1):
                nums[n-offset][j]=cnt
                cnt+=1
            #from bottom to top
            for i in range(n-offset,startx,-1):
                nums[i][starty]=cnt
                cnt+=1
            
            startx+=1
            starty+=1
        
        if n%2==1:
            nums[mid][mid]=cnt
        return nums



class Solution:
    def generateMatrix(self, n: int) -> List[List[int]]:
        A = [[0]*n for _ in range(n)]  
        i, j, di, dj = 0, 0, 0, 1
        for k in range(n*n):
            A[i][j] = k+1
            if A[(i+di)%n][(j+dj)%n]:
                di, dj = dj, -di
            
            i+=di
            j+=dj
        
        return A
