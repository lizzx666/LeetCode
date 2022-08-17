'''
You are given an array of integers nums, there is a sliding window of size k which is moving from the very left of the array to the very right. 
You can only see the k numbers in the window. Each time the sliding window moves right by one position.

Return the max sliding window.

 

Example 1:
Input: nums = [1,3,-1,-3,5,3,6,7], k = 3
Output: [3,3,5,5,6,7]
Explanation: 
Window position                Max
---------------               -----
[1  3  -1] -3  5  3  6  7       3
 1 [3  -1  -3] 5  3  6  7       3
 1  3 [-1  -3  5] 3  6  7       5
 1  3  -1 [-3  5  3] 6  7       5
 1  3  -1  -3 [5  3  6] 7       6
 1  3  -1  -3  5 [3  6  7]      7
 
 
Example 2:
Input: nums = [1], k = 1
Output: [1]

'''



class Solution:
    def __init__(self):
        self.queue = []
    
    def pop(self,value):
        if self.queue and value == self.queue[0]:
            self.queue.pop(0)
    
    def push(self,value):
        while self.queue and value > self.queue[-1]:
            self.queue.pop()
        self.queue.append(value)
    
    def getmax(self):
        return self.queue[0]
    
    
    
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        que = Solution()
        result = []
        for i in range(k):
            que.push(nums[i])
            
        result.append(que.getmax())
        for i in range(k,len(nums)):
            que.pop(nums[i-k])
            que.push(nums[i])
            result.append(que.getmax())
            
        return result
