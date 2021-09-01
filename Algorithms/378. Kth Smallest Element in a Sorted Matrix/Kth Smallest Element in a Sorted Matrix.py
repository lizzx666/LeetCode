'''
Given an n x n matrix where each of the rows and columns are sorted in ascending order, return the kth smallest element in the matrix.

Note that it is the kth smallest element in the sorted order, not the kth distinct element.

 

Example 1:
Input: matrix = [[1,5,9],[10,11,13],[12,13,15]], k = 8
Output: 13
Explanation: The elements in the matrix are [1,5,9,10,11,12,13,13,15], and the 8th smallest number is 13

Example 2:
Input: matrix = [[-5]], k = 1
Output: -5
'''
#heap
class Solution:
    def kthSmallest(self, matrix: List[List[int]], k: int) -> int:
        import heapq
        n = len(matrix)
        minheap = []
        for r in range(min(n,k)):
            minheap.append((matrix[r][0],r,0))
        heapq.heapify(minheap)
        while k:
            element, r, c = heapq.heappop(minheap)
            if c < n-1:
                heapq.heappush(minheap,(matrix[r][c+1],r,c+1))
            k -= 1
        return element
       
#binary search
class Solution:
    def countLessEqual(self,matrix,mid,smaller,larger):
        count, n = 0, len(matrix)
        row, col = n-1, 0 
        while row >= 0 and col < n:
            if matrix[row][col] > mid:
                larger = min(larger, matrix[row][col])
                row -= 1
            else:
                smaller = max(smaller, matrix[row][col])
                count += row+1
                col += 1
        return count, smaller, larger
    def kthSmallest(self, matrix: List[List[int]], k: int) -> int:

        n = len(matrix)
        start, end = matrix[0][0], matrix[n-1][n-1]
        while start < end:
            mid = start + (end-start)/2
            smaller, larger = matrix[0][0], matrix[n-1][n-1]
            count, smaller, larger = self.countLessEqual(matrix, mid, smaller, larger)
            if count == k :
                return smaller
            if count < k:
                start = larger
            else:
                end = smaller
        return start
