'''

Given an integer n, count the total number of digit 1 appearing in all non-negative integers less than or equal to n.

 

Example 1:
Input: n = 13
Output: 6

Example 2:
Input: n = 0
Output: 0

'''

class Solution:
    def countDigitOne(self, n: int) -> int:
        if n<=0:
            return 0
        q,x,ans = n,1,0
        while q>0:
            digit = q%10
            q = q//10
            ans += q*x
            if digit ==1:
                ans += n%x + 1
            elif digit >1:
                ans += x
            x*= 10
        return ans
