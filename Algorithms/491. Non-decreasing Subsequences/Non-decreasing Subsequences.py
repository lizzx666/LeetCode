'''

Given an integer array nums, return all the different possible non-decreasing subsequences of the given array with at least two elements. 
You may return the answer in any order.

 

Example 1:
Input: nums = [4,6,7,7]
Output: [[4,6],[4,6,7],[4,6,7,7],[4,7],[4,7,7],[6,7],[6,7,7],[7,7]]

Example 2:
Input: nums = [4,4,3,2,1]
Output: [[4,4]]


'''




class Solution:

    def findSubsequences(self, nums: List[int]) -> List[List[int]]:
        path = []
        res = []
        self.backtracking(nums,0,path,res)
        return res

    def backtracking(self,nums,start_index,path,res):
        if len(path)>1:
            res.append(path[:])
        
        uset = set()
        for i in range(start_index,len(nums)):
            if (len(path)>0 and path[-1]>nums[i]) or nums[i] in uset:
                continue
            uset.add(nums[i])
            path.append(nums[i])
            self.backtracking(nums,i+1,path,res)
            path.pop()
