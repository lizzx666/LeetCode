'''
Given a signed 32-bit integer x, return x with its digits reversed. 
If reversing x causes the value to go outside the signed 32-bit integer range [-2^31, 2^31 - 1], then return 0.

Assume the environment does not allow you to store 64-bit integers (signed or unsigned).

Example 1:
Input: x = 123
Output: 321

Example 2:
Input: x = -123
Output: -321

Example 3:
Input: x = 120
Output: 21

Example 4:
Input: x = 0
Output: 0
'''

#solution 1:
class Solution:
    def reverse(self, x: int) -> int:
        if x < 0:
            x1 = -int(str(-x)[::-1])
            if x1 < -2**31:
                return 0
            else:
                return x1
        else:
            x1 = int(str(x)[::-1])
            if x1 > 2**31-1:
                return 0
            else:
                return x1
            
#solution 2:           
class Solution:
    def reverse(self, x: int) -> int:
        sign = [1,-1][x<0]
        res = sign*int(str(abs(x))[::-1])
        return res if -2**31<=res<=2**31-1 else 0
