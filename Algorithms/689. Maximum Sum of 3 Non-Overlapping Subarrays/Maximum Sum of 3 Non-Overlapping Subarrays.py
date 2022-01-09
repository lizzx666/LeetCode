'''
Given an integer array nums and an integer k, find three non-overlapping subarrays of length k with maximum sum and return them.

Return the result as a list of indices representing the starting position of each interval (0-indexed). 
If there are multiple answers, return the lexicographically smallest one.

 

Example 1:

Input: nums = [1,2,1,2,6,7,5,1], k = 2
Output: [0,3,5]
Explanation: Subarrays [1, 2], [2, 6], [7, 5] correspond to the starting indices [0, 3, 5].
We could have also taken [2, 1], but an answer of [1, 3, 5] would be lexicographically larger.
Example 2:

Input: nums = [1,2,1,2,1,2,1,2,1], k = 2
Output: [0,2,4]

'''



class Solution:
    def maxSumOfThreeSubarrays(self, nums: List[int], k: int) -> List[int]:
        #array_1 : [0,k-1]
        #array_2 : [k,2k-1]
        #array_3 : [2k,3k-1]
        ans = []
        sum1, maxSum1, maxSum1Idx = 0,0,0
        sum2, maxSum12, maxSum12Idx = 0,0,()
        sum3, maxTotal = 0,0
        n = len(nums)
        for i in range(2*k,n):
            sum1 += nums[i-2*k]
            sum2 += nums[i-k]
            sum3 += nums[i]
            if i >= 3*k-1:
                if sum1 > maxSum1:
                    maxSum1 = sum1
                    maxSum1Idx = i-3*k+1
                if maxSum1 + sum2 > maxSum12:
                    maxSum12 = maxSum1 + sum2
                    maxSum12Idx = (maxSum1Idx,i-2*k+1)
                if maxSum12 + sum3 > maxTotal:
                    maxTotal = maxSum12 + sum3
                    ans = [*maxSum12Idx,i-k+1]
                sum1 -= nums[i-3*k+1]
                sum2 -= nums[i-2*k+1]
                sum3 -= nums[i-k+1]
        return ans
