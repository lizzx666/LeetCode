'''
Given two non-negative integers num1 and num2 represented as strings, return the product of num1 and num2, also represented as a string.

Note: You must not use any built-in BigInteger library or convert the inputs to integer directly.

 

Example 1:
Input: num1 = "2", num2 = "3"
Output: "6"

Example 2:
Input: num1 = "123", num2 = "456"
Output: "56088"


'''


class Solution:
    def multiply(self, num1: str, num2: str) -> str:
        if num1 == '0' or num2 =='0':
            return '0'
        m,n = len(num1), len(num2)
        ans = [0]*(m+n)
        for i in range(m-1,-1,-1):
            x = int(num1[i])
            for j in range(n-1,-1,-1):
                ans[i+j+1] += x*int(num2[j])
                
        for k in range(m+n-1,0,-1):
            ans[k-1] += ans[k]//10
            ans[k] %= 10
            
        index = 1 if ans[0]==0 else 0
        ans = ''.join(str(x) for x in ans[index:])
        return ans
