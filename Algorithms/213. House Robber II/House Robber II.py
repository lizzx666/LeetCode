'''

You are a professional robber planning to rob houses along a street. Each house has a certain amount of money stashed. 
All houses at this place are arranged in a circle. That means the first house is the neighbor of the last one. 
Meanwhile, adjacent houses have a security system connected, and it will automatically contact the police if two adjacent houses were broken into on the same night.

Given an integer array nums representing the amount of money of each house, return the maximum amount of money you can rob tonight without alerting the police.



Example 1:
Input: nums = [2,3,2]
Output: 3
Explanation: You cannot rob house 1 (money = 2) and then rob house 3 (money = 2), because they are adjacent houses.

Example 2:
Input: nums = [1,2,3,1]
Output: 4
Explanation: Rob house 1 (money = 1) and then rob house 3 (money = 3).
Total amount you can rob = 1 + 3 = 4.

Example 3:
Input: nums = [0]
Output: 0

'''



class Solution:
    def rob(self, nums: List[int]) -> int:
        #to deal with circle
        #we can make it a linear list(house rob i) by only considering non-head part or only consider non-tail part
        #then take the best out of these 2 situations
        if len(nums)==1:
            return nums[0]
        head_nums = nums[:-1]
        tail_nums = nums[1:]

        max_head = self.rob_func(head_nums)
        max_tail = self.rob_func(tail_nums)

        return max(max_head,max_tail)

    def rob_func(self,nums):
        if len(nums)==1:
            return nums[0]
        dp = [0]*len(nums)
        dp[0] = nums[0]
        dp[1] = max(nums[0],nums[1])

        for i in range(2,len(nums)):
            dp[i] = max(dp[i-2]+nums[i],dp[i-1])
        return dp[-1]




class Solution:
    def rob(self, nums: List[int]) -> int:
        if not nums:
            return 0
        elif len(nums)==1:
            return nums[0]
        else:
            N = len(nums)
            nums_1 = nums[1:]
            nums_2 = nums[:N-1]
            rob_1 = [0]*N
            rob_2 = [0]*N
            rob_1[N-1],rob_1[N-2] = 0,nums_1[N-2]
            rob_2[N-1],rob_2[N-2] = 0,nums_2[N-2]
            for i in range(N-3,-1,-1):
                rob_1[i] = max(rob_1[i+1],rob_1[i+2]+nums_1[i])
                rob_2[i] = max(rob_2[i+1],rob_2[i+2]+nums[i])
    
            return max(rob_1[0],rob_2[0])
