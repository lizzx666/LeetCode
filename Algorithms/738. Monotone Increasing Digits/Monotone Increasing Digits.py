'''

An integer has monotone increasing digits if and only if each pair of adjacent digits x and y satisfy x <= y.

Given an integer n, return the largest number that is less than or equal to n with monotone increasing digits.

 

Example 1:

Input: n = 10
Output: 9
Example 2:

Input: n = 1234
Output: 1234
Example 3:

Input: n = 332
Output: 299


'''



class Solution:
    def monotoneIncreasingDigits(self, n: int) -> int:
        st = list(str(n))

        for i in range(len(st)-1,0,-1):
            if int(st[i])<int(st[i-1]):
                st[i-1] = str(int(st[i-1])-1)
                st[i:] = '9'*(len(st) - i)

        return int("".join(st))
