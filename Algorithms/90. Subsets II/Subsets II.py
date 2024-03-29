'''


Given an integer array nums that may contain duplicates, return all possible subsets (the power set).

The solution set must not contain duplicate subsets. Return the solution in any order.

 

Example 1:
Input: nums = [1,2,2]
Output: [[],[1],[1,2],[1,2,2],[2],[2,2]]


Example 2:
Input: nums = [0]
Output: [[],[0]]


'''

class Solution:
    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
        if not nums:
            return []
        nums.sort()
        res, cur = [[]], []
        for i in range(len(nums)):

            if i>0 and nums[i]==nums[i-1]:

                cur = [item + [nums[i]] for item in cur]

            else:
                cur = [item + [nums[i]] for item in res]

            
            res += cur
        return res
