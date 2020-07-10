class Solution:
    def nextPermutation(self, nums: List[int]) -> None:
        k, l = len(nums) -2 , len(nums) - 1 
        while k >= 0 and nums[k] >= nums[k+1]: 
            k -= 1 
        if k == -1: 
            return nums.reverse() 
        while nums[k] >= nums[l]:  
            l -= 1  
        nums[k], nums[l] = nums[l], nums[k]  
        nums[k+1:]=reversed(nums[k+1:])  
