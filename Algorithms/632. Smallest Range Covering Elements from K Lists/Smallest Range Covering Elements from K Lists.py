'''
You have k lists of sorted integers in non-decreasing order. Find the smallest range that includes at least one number from each of the k lists.

We define the range [a, b] is smaller than range [c, d] if b - a < d - c or a < c if b - a == d - c.

 

Example 1:

Input: nums = [[4,10,15,24,26],[0,9,12,20],[5,18,22,30]]
Output: [20,24]
Explanation: 
List 1: [4, 10, 15, 24,26], 24 is in range [20,24].
List 2: [0, 9, 12, 20], 20 is in range [20,24].
List 3: [5, 18, 22, 30], 22 is in range [20,24].

Example 2:
Input: nums = [[1,2,3],[1,2,3],[1,2,3]]
Output: [1,1]

'''
'''
The question is equal to pick k number from k sorted list, and need to ensure the difference between max and min of these k numbers are smallest
'''


class Solution:
    def smallestRange(self, nums: List[List[int]]) -> List[int]:
        range_left, range_right = -1e9,1e9
        max_value = max(vec[0] for vec in nums)
        pq = [(vec[0],i,0) for i,vec in enumerate(nums)]
        heapq.heapify(pq)
        
        while True:
            min_value, row, idx = heapq.heappop(pq)
            if max_value - min_value < range_right - range_left:
                range_left, range_right = min_value, max_value
            if idx == len(nums[row])-1:
                break
            max_value = max(max_value, nums[row][idx+1])
            heapq.heappush(pq, (nums[row][idx+1],row,idx+1))
        
        return [range_left,range_right]
