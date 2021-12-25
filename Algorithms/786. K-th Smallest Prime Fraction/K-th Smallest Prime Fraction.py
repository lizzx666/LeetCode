'''
You are given a sorted integer array arr containing 1 and prime numbers, where all the integers of arr are unique. You are also given an integer k.

For every i and j where 0 <= i < j < arr.length, we consider the fraction arr[i] / arr[j].

Return the kth smallest fraction considered. Return your answer as an array of integers of size 2, where answer[0] == arr[i] and answer[1] == arr[j].

 

Example 1:

Input: arr = [1,2,3,5], k = 3
Output: [2,5]
Explanation: The fractions to be considered in sorted order are:
1/5, 1/3, 2/5, 1/2, 3/5, and 2/3.
The third fraction is 2/5.
Example 2:

Input: arr = [1,7], k = 1
Output: [1,7]

'''
#Binary Search + Double Pointer
class Solution:
    def kthSmallestPrimeFraction(self, arr: List[int], k: int) -> List[int]:
        #find a number that exactly K prime fractions smaller than this number
        #and the kth of this fractions is the number we want
        
        n = len(arr)
        left, right = 0.0, 1.0
        while True:
            mid = (left + right)/2
            i, count = -1,0
            x,y = 0,1
            for j in range(1,n):
                
                while arr[i+1]/arr[j] < mid:
                    i+=1
                    #update max fraction
                    if arr[i]*y>arr[j]*x: #arr[i]/arr[j] > x/y
                        x,y = arr[i],arr[j]
                count += i+1
        
            if count == k:
                return [x,y]
        
            elif count < k:
                left = mid
            
            else:
                right = mid



#Brute Force
class Solution:
    def kthSmallestPrimeFraction(self, arr: List[int], k: int) -> List[int]:
        import heapq
        n = len(arr)
        s = {}
        for i in range(n-1):
            for j in range(i+1,n):
                s[arr[i],arr[j]] = arr[i]/arr[j]      
        return heapq.nsmallest(k,s,key = s.get)[-1]
