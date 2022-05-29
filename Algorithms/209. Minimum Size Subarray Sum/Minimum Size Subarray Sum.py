'''

Given an array of positive integers nums and a positive integer target, 
return the minimal length of a contiguous subarray [numsl, numsl+1, ..., numsr-1, numsr] of which the sum is greater than or equal to target. 
If there is no such subarray, return 0 instead.

 

Example 1:

Input: target = 7, nums = [2,3,1,2,4,3]
Output: 2
Explanation: The subarray [4,3] has the minimal length under the problem constraint.

Example 2:
Input: target = 4, nums = [1,4,4]
Output: 1

Example 3:
Input: target = 11, nums = [1,1,1,1,1,1,1,1]
Output: 0

'''


class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:
        n = len(nums)
        min_cnt = n+1

        left = 0
        curr_sum = 0
        
        for i in range(n):
            curr_sum += nums[i]
            while curr_sum >= target:
                min_cnt = min(min_cnt,i-left+1)
                curr_sum -= nums[left]
                left+=1
        return min_cnt if min_cnt<= n else 0
