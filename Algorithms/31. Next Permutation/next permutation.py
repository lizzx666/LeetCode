'''
Implement next permutation, which rearranges numbers into the lexicographically next greater permutation of numbers.

If such arrangement is not possible, it must rearrange it as the lowest possible order (ie, sorted in ascending order).

The replacement must be in-place and use only constant extra memory.

Here are some examples. Inputs are in the left-hand column and its corresponding outputs are in the right-hand column.

[1,2,3] → [1,3,2]
[3,2,1] → [1,2,3]
[1,1,5] → [1,5,1]

'''





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
