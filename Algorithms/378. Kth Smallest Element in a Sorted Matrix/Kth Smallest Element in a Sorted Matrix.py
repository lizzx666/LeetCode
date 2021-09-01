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
