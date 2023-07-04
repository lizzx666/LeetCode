'''
Given an integer array nums, return true if you can partition the array into two subsets such that the sum of the elements in both subsets is equal or false otherwise.

 

Example 1:
Input: nums = [1,5,11,5]
Output: true
Explanation: The array can be partitioned as [1, 5, 5] and [11].

Example 2:
Input: nums = [1,2,3,5]
Output: false
Explanation: The array cannot be partitioned into equal sum subsets.



'''



class Solution:
    def canPartition(self, nums: List[int]) -> bool:
        sum_nums = sum(nums)
        if sum_nums%2:
            return False

        target = sum_nums//2

        dp = [0]*(target+1)

        for i in range(len(nums)):
            for j in range(target,nums[i]-1,-1):
                dp[j] = max(dp[j],dp[j-nums[i]]+nums[i])
                #print(dp)
        #print(dp)
        if dp[target]==target:
            return True
        else:
            return False
