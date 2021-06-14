'''
Write an efficient algorithm that searches for a value in an m x n matrix. This matrix has the following properties:

Integers in each row are sorted from left to right.
The first integer of each row is greater than the last integer of the previous row.

Input: matrix = [[1,3,5,7],[10,11,16,20],[23,30,34,60]], target = 3
Output: true


'''



def searchMatrix(matrix, target):
    m = len(matrix)
    n = len(matrix[0])
    left,right = 0, m*n-1
    while left <= right:
        pivot_index = (left+right)/2
        #x//y round down to the nearest integer
        pivot_element = matrix[pivot_index // n][pivot_index % n]
        if target == pivot_element:
            return True
        else:
            if target< pivot_element:
                right = pivot_index - 1
            else:
                left = pivot_index + 1
    return False
