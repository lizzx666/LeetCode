'''

You are given a string num representing the digits of a very large integer and an integer k. 
You are allowed to swap any two adjacent digits of the integer at most k times.

Return the minimum integer you can obtain also as a string.

 

Example 1:
Input: num = "4321", k = 4
Output: "1342"
Explanation: The steps to obtain the minimum integer from 4321 with 4 adjacent swaps are shown.

Example 2:
Input: num = "100", k = 1
Output: "010"
Explanation: It's ok for the output to have leading zeros, but the input is guaranteed not to have any leading zeros.

Example 3:
Input: num = "36789", k = 1000
Output: "36789"
Explanation: We can keep the number without any swaps.

'''

#Brute Force
#O(n^2), O(n)

class Solution:
    def minInteger(self, num: str, k: int) -> str:
        if k<=0:
            return num
        n = len(num)
        if k>= n*(n-1)//2:
            return "".join(sorted(list(num)))
        
        for i in range(10):
            ind = num.find(str(i))
            if 0<=ind<=k:
                return str(num[ind]) + self.minInteger(num[0:ind] + num[ind+1:], k-ind)
