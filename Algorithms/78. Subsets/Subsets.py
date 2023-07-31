'''

Given an integer array nums of unique elements, return all possible subsets (the power set).

The solution set must not contain duplicate subsets. Return the solution in any order.

 

Example 1:
Input: nums = [1,2,3]
Output: [[],[1],[2],[1,2],[3],[1,3],[2,3],[1,2,3]]



Example 2:
Input: nums = [0]
Output: [[],[0]]

'''




class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        path = []
        res = []
        self.backtracking(nums,0,path,res)
        return res

    
    def backtracking(self,nums,start_index,path,res):
        res.append(path[:])
        if start_index >= len(nums): #actually can skip
            return
        
        for i in range(start_index,len(nums)):
            path.append(nums[i])
            self.backtracking(nums,i+1,path,res)
            path.pop()






class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        
        n = len(nums)
        output = [[]]
        
        for num in nums:
            output += [curr + [num] for curr in output]
            
        return output
