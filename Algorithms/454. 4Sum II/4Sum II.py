'''
Given four integer arrays nums1, nums2, nums3, and nums4 all of length n, return the number of tuples (i, j, k, l) such that:

0 <= i, j, k, l < n
nums1[i] + nums2[j] + nums3[k] + nums4[l] == 0
 

Example 1:
Input: nums1 = [1,2], nums2 = [-2,-1], nums3 = [-1,2], nums4 = [0,2]
Output: 2
Explanation:
The two tuples are:
1. (0, 0, 0, 1) -> nums1[0] + nums2[0] + nums3[0] + nums4[1] = 1 + (-2) + (-1) + 2 = 0
2. (1, 1, 0, 0) -> nums1[1] + nums2[1] + nums3[0] + nums4[0] = 2 + (-1) + (-1) + 0 = 0

Example 2:
Input: nums1 = [0], nums2 = [0], nums3 = [0], nums4 = [0]
Output: 1

'''


class Solution:
    def fourSumCount(self, nums1: List[int], nums2: List[int], nums3: List[int], nums4: List[int]) -> int:
        d1 = collections.defaultdict(int)
        cnt = 0
        for a in nums1:
            for b in nums2:
                d1[a+b]+=1
        
        for c in nums3:
            for d in nums4:
                cnt+=d1[-(c+d)]
        return cnt



class Solution:
    def fourSumCount(self, nums1: List[int], nums2: List[int], nums3: List[int], nums4: List[int]) -> int:
        n = len(nums1)
        d = {}
        cnt = 0
        for i in range(n):
            for j in range(n):
                if nums1[i]+nums2[j] in d.keys():
                    d[nums1[i]+nums2[j]]+=1
                else:
                    d[nums1[i]+nums2[j]]=1
        
        for i in range(n):
            for j in range(n):
                if 0-(nums3[i]+nums4[j]) in d.keys():
                    cnt+=d[0-(nums3[i]+nums4[j])]
        return cnt
