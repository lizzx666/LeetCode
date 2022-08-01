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
        result = []
        n = len(nums)
        for i in range(n):

            if nums[i]>0:
                break
            if i>0 and nums[i-1]==nums[i]:
                continue
            left = i+1
            right = n-1

            while left<right:
                if nums[i]+nums[left]+nums[right]<0:
                    left+=1
                elif nums[i]+nums[left]+nums[right]>0:
                    right-=1
                else:
                    result.append([nums[i],nums[left],nums[right]])
                    while left<right and nums[left]==nums[left+1]:
                        left+=1
                    while left<right and nums[right]==nums[right-1]:
                        right-=1
                    
                    left+=1
                    right-=1
        return result





class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        n = len(nums)
        result = []
        for first in range(n-2):
            if first>0 and nums[first]==nums[first-1]:
                continue
            second = first+1
            third = n-1
            while second<third:
                s = nums[first]+nums[second]+nums[third]
                if s < 0:
                    second+=1
                elif s>0:
                    third-=1
                else:
                    result.append([nums[first],nums[second],nums[third]])
                    while second < third and nums[second+1]==nums[second]:
                        second+=1
                    while second < third and nums[third-1]==nums[third]:
                        third-=1
                    third-=1
                    second+=1
                    
        return result
       
       
       
       
       
       

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
