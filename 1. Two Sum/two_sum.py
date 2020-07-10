class Solution(object):
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        dict1 = {}
        for i,num in enumerate(nums):
            tar_num = target - num
            if tar_num in dict1:
                return [dict1[tar_num],i]
            dict1[num] = i
