'''

Given a circular integer array nums (i.e., the next element of nums[nums.length - 1] is nums[0]), return the next greater number for every element in nums.

The next greater number of a number x is the first greater number to its traversing-order next in the array, 
which means you could search circularly to find its next greater number. If it doesn't exist, return -1 for this number.

 

Example 1:
Input: nums = [1,2,1]
Output: [2,-1,2]
Explanation: The first 1's next greater number is 2; 
The number 2 can't find next greater number. 
The second 1's next greater number needs to search circularly, which is also 2.

Example 2:
Input: nums = [1,2,3,4,3]
Output: [2,3,4,-1,4]


'''

#method 2
class Solution:
    def nextGreaterElements(self, nums: List[int]) -> List[int]:
        res = [-1]*len(nums)
        stk = [0]

        for i in range(1,len(nums)*2):
            j = i%(len(nums))
            if nums[j]<=nums[stk[-1]]:
                stk.append(j)    

            else:
                while stk and nums[j]>nums[stk[-1]]:
                    res[stk[-1]] = nums[j] 
                    stk.pop()
                stk.append(j)
        return res   


#method 1
class Solution:
    def nextGreaterElements(self, nums: List[int]) -> List[int]:
        new_nums = nums+nums
        stk = [0]
        res = [-1]*len(new_nums)

        for i in range(1,len(new_nums)):
            if new_nums[i]<=new_nums[stk[-1]]:
                stk.append(i)
            else:
                while stk and new_nums[i]>new_nums[stk[-1]]:
                    res[stk[-1]]=new_nums[i]
                    stk.pop()
                stk.append(i)
        return res[:len(nums)]
