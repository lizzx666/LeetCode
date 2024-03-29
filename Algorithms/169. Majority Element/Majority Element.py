'''
Given an array nums of size n, return the majority element.

The majority element is the element that appears more than ⌊n / 2⌋ times. You may assume that the majority element always exists in the array.

 

Example 1:
Input: nums = [3,2,3]
Output: 3

Example 2:
Input: nums = [2,2,1,1,1,2,2]
Output: 2

'''


class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        from collections import Counter
        dict_1 = Counter(nums)
        return [k for k,v in dict_1.items() if v>= len(nums)/2][0]
  
  
class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        from collections import Counter
        dict_1 = Counter(nums)
        return max(dict_1.keys(), key = dict_1.get)
