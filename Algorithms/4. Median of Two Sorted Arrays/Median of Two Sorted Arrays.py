'''
Given two sorted arrays nums1 and nums2 of size m and n respectively, return the median of the two sorted arrays.

The overall run time complexity should be O(log (m+n)).

 

Example 1:
Input: nums1 = [1,3], nums2 = [2]
Output: 2.00000
Explanation: merged array = [1,2,3] and median is 2.

Example 2:
Input: nums1 = [1,2], nums2 = [3,4]
Output: 2.50000
Explanation: merged array = [1,2,3,4] and median is (2 + 3) / 2 = 2.5.

'''

class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        if len(nums1) > len(nums2):
            temp = nums1
            nums1 = nums2
            nums2 = temp
        m = len(nums1)
        n = len(nums2)
        '''
        if m==0:
            if n %2 ==1:
                return nums2[n//2]
            else:
                return (nums2[n//2] + nums2[(n+1)//2])/2
        '''
        #total_left_count = (n+m+1)/2
        #if (n+m)%2==0 then total_left should be (n+m)/2 which is same as (n+m+1)//2
        #if (n+m)%2==1 then total_left should be (n+m+1)//2
        total_left = (n+m+1)//2
        
        #i is the first element at cut line right side for nums1
        #j is the first element at cut line right side for nums2
        #need to satisfy nums1[i-1] <= nums2[j] and nums2[j-1] <= nums1[i]
        #i + j = (n+m+1)//2
        
        left = 0
        right = m
        while left < right:
            #i = left + (right-left + 1)//2
            i = left + (right-left)//2
            j = total_left - i
            
            #if nums1[i-1] > nums2[j]:
            if nums2[j-1] > nums1[i]:
                #cut line set too right for nums1
                #next search range [left,i-1]
                #right = i-1
                #next search range [i+1,right]
                left = i+1
            else:
                #next search range[i,right]
            #if enter [left(i),right], the range won't be reduced any longer and will enter a endless loop
            #so make i = left + (right-left+1)//2
                #left = i
                #next search range [left,i]
                right = i
        
        i = left
        j = total_left - i
        nums1_leftmax = float('-inf') if i==0 else nums1[i-1]
        nums1_rightmin = float('inf') if i==m else nums1[i]
        nums2_leftmax = float('-inf') if j==0 else nums2[j-1]
        nums2_rightmin = float('inf') if j==n else nums2[j] 
        
        if (m+n)%2==1:
            return max(nums1_leftmax,nums2_leftmax)
        else:
            return (max(nums1_leftmax,nums2_leftmax)+min(nums1_rightmin,nums2_rightmin))/2
