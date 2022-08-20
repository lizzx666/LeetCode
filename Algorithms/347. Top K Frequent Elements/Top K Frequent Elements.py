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



class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        import collections
        d = collections.Counter(nums)
        
        pri_que = []
        for key,freq in d.items():
            heapq.heappush(pri_que,(freq,key))
            if len(pri_que) > k:
                heapq.heappop(pri_que)
        
        result = [0]*k
        for i in range(k-1,-1,-1):
            result[i] = heapq.heappop(pri_que)[1]
        return result
    
    

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

#Method 3
def topKFrequent(nums,k):
    import collections 
    import itertools
    bucket = [[] for i in range(len(nums)+1)]
    count = collections.Counter(nums).items()
    for num, freq in count:
        bucket[freq].append(num)
    flat_list = list(itertools.chain(*bucket))
    return flat_list[::-1][:k]
