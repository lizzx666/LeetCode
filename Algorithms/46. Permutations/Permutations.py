'''
Given an array nums of distinct integers, return all the possible permutations. You can return the answer in any order.

 

Example 1:
Input: nums = [1,2,3]
Output: [[1,2,3],[1,3,2],[2,1,3],[2,3,1],[3,1,2],[3,2,1]]

Example 2:
Input: nums = [0,1]
Output: [[0,1],[1,0]]

Example 3:
Input: nums = [1]
Output: [[1]]



'''




class Solution:
    
    def permute(self, nums: List[int]) -> List[List[int]]:
        path = []
        res = []
        used = [0]*len(nums)
        self.backtracking(nums,used,path,res)
        return res
    
    def backtracking(self,nums,used,path,res):
        if len(path)==len(nums):
            res.append(path[:])
            return
        for i in range(len(nums)):
            if used[i]==1:
                continue
            used[i]=1
            path.append(nums[i])
            self.backtracking(nums,used,path,res)
            used[i]=0
            path.pop()
