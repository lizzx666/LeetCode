'''
Given an array of non-negative integers nums, you are initially positioned at the first index of the array.

Each element in the array represents your maximum jump length at that position.

Your goal is to reach the last index in the minimum number of jumps.

You can assume that you can always reach the last index.

 

Example 1:
Input: nums = [2,3,1,1,4]
Output: 2
Explanation: The minimum number of jumps to reach the last index is 2. Jump 1 step from index 0 to 1, then 3 steps to the last index.

Example 2:
Input: nums = [2,3,0,1,4]
Output: 2

'''


class Solution:
    def jump(self, nums: List[int]) -> int:
        if len(nums)==1:
            return 0
        cur_cover = 0
        next_cover = 0   
        result = 0
        for i in range(len(nums)):
            next_cover = max(next_cover,i+nums[i])
            if i==cur_cover:
                if cur_cover < len(nums)-1:
                    result+=1 
                    cur_cover = next_cover  
                    if cur_cover >= len(nums)-1:
                        break
        return result
       
       
       

class Solution:
    def jump(self, nums: List[int]) -> int:
        n = len(nums)
        start, end, step = 0,0,0
        while end < n-1:
            step+=1
            max_end = end+1
            for i in range(start,end+1):
                if i+nums[i]>n-1:
                    return step
                max_end = max(max_end,i+nums[i])
            start,end = end+1,max_end
        return step
