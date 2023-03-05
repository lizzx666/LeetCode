'''
Count the number of prime numbers less than a non-negative number, n.

Example 1:
Input: n = 10
Output: 4
Explanation: There are 4 prime numbers less than 10, they are 2, 3, 5, 7.

Example 2:
Input: n = 0
Output: 0

Example 3:
Input: n = 1
Output: 0

'''



class Solution:
    def countPrimes(self, n: int) -> int:
        from math import sqrt
        if n <=2:
            return 0
        nums = [0,0] + [1] * (n-2)
        for p in range(2,int(sqrt(n)) + 1):
            if nums[p]:
                for multiple in range(p*p,n,p):
                    nums[multiple] = 0
        return sum(nums)
    
    








class Solution:
    def countPrimes(self, n: int) -> int:
        from math import sqrt
        if n<=2:
            return 0
        numbers = {}
        for i in range(2,int(sqrt(n))+1):
            if i not in numbers:
                for multiple in range(i*i,n,i):
                    numbers[multiple]=1
        return n - 2 - len(numbers)
