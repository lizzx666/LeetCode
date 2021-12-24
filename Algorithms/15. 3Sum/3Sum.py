'''

Given an integer array nums, return all the triplets [nums[i], nums[j], nums[k]] such that i != j, i != k, and j != k, and nums[i] + nums[j] + nums[k] == 0.

Notice that the solution set must not contain duplicate triplets.

 

Example 1:
Input: nums = [-1,0,1,2,-1,-4]
Output: [[-1,-1,2],[-1,0,1]]

Example 2:
Input: nums = []
Output: []

Example 3:
Input: nums = [0]
Output: []

'''



class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        output = []
        n = len(nums)
        for first in range(n):
            if first > 0 and nums[first] == nums[first-1]:
                continue
            third = n-1
            target = -nums[first]
            for second in range(first+1,n):
                if second > first+1 and nums[second] == nums[second-1]:
                    continue
                while second < third and nums[second] + nums[third] > target:
                    third -= 1
                
                if second == third:
                    break
                if nums[second] + nums[third]==target:
                    output.append([nums[first], nums[second], nums[third]])
                    
        return output
