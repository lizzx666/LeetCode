'''
Given an m x n matrix, return all elements of the matrix in spiral order.

Example 1:

Input: matrix = [[1,2,3],[4,5,6],[7,8,9]]
Output: [1,2,3,6,9,8,7,4,5]

Example 2:
Input: matrix = [[1,2,3,4],[5,6,7,8],[9,10,11,12]]
Output: [1,2,3,4,8,12,11,10,9,5,6,7]


'''

#own solution
def spiralOrder(matrix):
    new = []
    m = len(matrix)
    n = len(matrix[0])
    up,down =0, m-1
    left,right = 0,n-1
    while up<=down and left<=right and len(new)<m*n:
        #top left to right
        
        new.extend(matrix[up][left:right+1])
 
        
        #right up to down
        new.extend(row[right] for row in matrix[up+1:down+1])

        
        if up!=down:
        #bottom right to left
            new.extend(matrix[down][left:right][::-1])


        #left down to up
        if left !=right:
            new.extend(row[left] for row in matrix[up+1:down][::-1])
            
        left +=1
        right -=1
        up+=1
        down -=1


    return new


#answer
class Solution:
    def spiralOrder(self, matrix: List[List[int]]) -> List[int]:
        result = []
        rows, columns = len(matrix), len(matrix[0])
        up = left = 0
        right = columns - 1
        down = rows - 1
        while len(result) < rows * columns:
            for col in range(left,right+1):
                result.append(matrix[up][col])
        
            for row in range(up+1,down+1):
                result.append(matrix[row][right])
            
            if up!=down:
                for col in range(right-1, left-1, -1):
                    result.append(matrix[down][col])
            if left!= right:
                for row in range(down-1, up, -1):
                    result.append(matrix[row][left])
            left+=1
            right-=1
            up+=1
            down-=1
        return result
