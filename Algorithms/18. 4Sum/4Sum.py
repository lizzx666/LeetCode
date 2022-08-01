"""
Given an array nums of n integers, return an array of all the unique quadruplets [nums[a], nums[b], nums[c], nums[d]] such that:

0 <= a, b, c, d < n
a, b, c, and d are distinct.
nums[a] + nums[b] + nums[c] + nums[d] == target
You may return the answer in any order.

 

Example 1:

Input: nums = [1,0,-1,0,-2,2], target = 0
Output: [[-2,-1,1,2],[-2,0,0,2],[-1,0,0,1]]


Example 2:

Input: nums = [2,2,2,2,2], target = 8
Output: [[2,2,2,2]]

"""


class Solution:
    def fourSum(self, nums: List[int], target: int) -> List[List[int]]:
        nums.sort()
        result = []
        n = len(nums)
        
        for k in range(n):
            if nums[k]>target and target>=0:
                break
            if k>0 and nums[k-1]==nums[k]:
                continue
            for i in range(k+1,n):
                if nums[k]+nums[i]>target and target>=0:
                    break
                if i>k+1 and nums[i-1]==nums[i]:
                    continue
                left = i+1
                right = n-1
                while left<right:
                    total = nums[k]+nums[i]+nums[left]+nums[right]
                    if total<target:
                        left+=1
                    elif total>target:
                        right-=1
                    else:
                        result.append([nums[k],nums[i],nums[left],nums[right]])
                        while left<right and nums[left]==nums[left+1]:
                            left+=1
                        while left<right and nums[right]==nums[right-1]:
                            right-=1
                        left+=1
                        right-=1
        return result




def fourSum(nums, target):
      
    def KSum(nums, target, k, result, results):
        if len(nums)<k or k<2 or target < nums[0]*k or target > nums[-1]*k:
            return
        if k==2:
            l,r = 0, len(nums)-1
            while l<r:
                s = nums[l] + nums[r]
                if s==target:
                    results.append(result + [nums[l],nums[r]])
                    l += 1
                    while l<r and nums[l]==nums[l-1]:
                        l += 1
                elif s<target:
                    l += 1
                else:
                    r -= 1
        else:
            for i in range(len(nums)-k+1):
                if i==0 or (i>0 and nums[i-1] != nums[i]):
                    KSum(nums[i+1:], target-nums[i],k-1,result+[nums[i]], results)
                    
    results = []
    KSum(sorted(nums),target,4,[],results)
    return results
