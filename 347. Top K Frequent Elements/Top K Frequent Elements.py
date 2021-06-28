'''
Given an integer array nums and an integer k, return the k most frequent elements. 
You may return the answer in any order.

Example 1:
Input: nums = [1,1,1,2,2,3], k = 2
Output: [1,2]

Example 2:
Input: nums = [1], k = 1
Output: [1]

'''


#Method 1
def topKFrequent(nums,k):
    s = []
    import collections 
    counts = collections.Counter(nums)
    sort_counts = sorted(counts.items(), key = lambda x: x[1], reverse = True)
    for i in sort_counts:
        s.append(i[0])
    return s[:k]


#Method 2
def topKFrequent(nums,k):
    import collections 
    import heapq
    if k == len(nums):
        return nums
    counts = collections.Counter(nums)
    return heapq.nlargest(k,counts.keys(),key=counts.get)
