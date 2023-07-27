'''


Given a collection of candidate numbers (candidates) and a target number (target), find all unique combinations in candidates where the candidate numbers sum to target.

Each number in candidates may only be used once in the combination.

Note: The solution set must not contain duplicate combinations.

 

Example 1:

Input: candidates = [10,1,2,7,6,1,5], target = 8
Output: 
[
[1,1,6],
[1,2,5],
[1,7],
[2,6]
]

Example 2:
Input: candidates = [2,5,2,1,2], target = 5
Output: 
[
[1,2,2],
[5]
]


'''




class Solution:
    def __init__(self):
        self.result = []
        self.path = []
        self.cur_sum = 0
        
    def backtracking(self,candidates,target,cur_sum,start_index,used):
        if self.cur_sum>target:
            return
        if self.cur_sum==target:
            self.result.append(self.path[:])
            return
        
        for i in range(start_index,len(candidates)):
            if i>0 and candidates[i]==candidates[i-1] and used[i-1]==0:
                continue
            if self.cur_sum + candidates[i]>target:
                break

            self.path.append(candidates[i])
            self.cur_sum+=candidates[i]
            used[i]=1
            self.backtracking(candidates,target,self.cur_sum,i+1,used)
            self.path.pop()
            self.cur_sum-=candidates[i]
            used[i]=0

    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        candidates.sort()
        used = len(candidates)*[0]
        self.backtracking(candidates,target,self.cur_sum,0,used)
        return self.result
