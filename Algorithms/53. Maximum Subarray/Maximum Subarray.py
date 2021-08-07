'''
Given an integer array nums, find the contiguous subarray (containing at least one number) which has the largest sum and return its sum.

A subarray is a contiguous part of an array.

 

Example 1:
Input: nums = [-2,1,-3,4,-1,2,1,-5,4]
Output: 6
Explanation: [4,-1,2,1] has the largest sum = 6.

Example 2:
Input: nums = [1]
Output: 1

Example 3:
Input: nums = [5,4,-1,7,8]
Output: 23

'''
#Brute Force
class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        max_subarray = -math.inf
        for i in range(0,len(nums)):
            current_subarray = 0
            for j in range(i,len(nums)):
                current_subarray += nums[j]
                max_subarray = max(max_subarray,current_subarray)
        return max_subarray
       
       
#DP
    def maxSubArray(self, nums: List[int]) -> int:
        current_subarray = max_subarray = nums[0]
        for num in nums[1:]:
            current_subarray = max(current_subarray+num,num)
            max_subarray = max(current_subarray,max_subarray)
        return max_subarray
