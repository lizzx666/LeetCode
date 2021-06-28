'''
Given two integer arrays nums1 and nums2, return an array of their intersection. 
Each element in the result must be unique and you may return the result in any order.

 

Example 1:
Input: nums1 = [1,2,2,1], nums2 = [2,2]
Output: [2]

Example 2:
Input: nums1 = [4,9,5], nums2 = [9,4,9,8,4]
Output: [9,4]
Explanation: [4,9] is also accepted.


'''


def intersection(nums1,nums2):
    n = []
    k = set(nums1)
    m = set(nums2)
    if len(k) < len(m):
      for i in k:
        if i in m:
          n.append(i)
    return list(set(n))
    else:
      for i in m:
        if i in k:
          n.append(i)
    return list(set(n))

#or
def intersection(nums1,nums2):  
  k = set(nums1)
  m = set(nums2)
  return list (k & m)
