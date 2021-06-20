"""
Given an array of integers nums containing n + 1 integers where each integer is in the range [1, n] inclusive.

There is only one repeated number in nums, return this repeated number.

You must solve the problem without modifying the array nums and uses only constant extra space.

 

Example 1:
Input: nums = [1,3,4,2,2]
Output: 2


Example 2:
Input: nums = [3,1,3,4,2]
Output: 3


Example 3:
Input: nums = [1,1]
Output: 1


Example 4:
Input: nums = [1,1,2]
Output: 1

"""


#method 1
def findDuplicate(self, nums: List[int]) -> int:
 nums.sort()
 for i in range(len(nums)):
  if nums[i]==nums[i+1]:
   return nums[i]

  
  
#method 2:
def findDuplicate(self, nums: List[int]) -> int:
 unique = set()
 for num in nums:
  if num in unique:
   return num
  unique.add(num)
