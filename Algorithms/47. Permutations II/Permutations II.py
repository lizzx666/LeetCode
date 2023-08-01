'''


Given a collection of numbers, nums, that might contain duplicates, return all possible unique permutations in any order.

 

Example 1:
Input: nums = [1,1,2]
Output:
[[1,1,2],
 [1,2,1],
 [2,1,1]]
 
Example 2:
Input: nums = [1,2,3]
Output: [[1,2,3],[1,3,2],[2,1,3],[2,3,1],[3,1,2],[3,2,1]]


'''



class Solution:
    def permuteUnique(self, nums: List[int]) -> List[List[int]]:
        path = []
        res = []
        used = [0]*len(nums)
        nums.sort()
        self.backtracking(nums,used,path,res)
        return res
    
    def backtracking(self,nums,used,path,res):
        if len(path)==len(nums):
            res.append(path[:])
            return
        
        for i in range(len(nums)):
            if (i>0 and nums[i]==nums[i-1] and used[i-1]==0) or used[i]==1:
                continue
            used[i]=1
            path.append(nums[i])
            self.backtracking(nums,used,path,res)
            used[i]=0
            path.pop()
