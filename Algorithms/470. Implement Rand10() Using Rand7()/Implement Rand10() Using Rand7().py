'''
Given the API rand7() that generates a uniform random integer in the range [1, 7], 
write a function rand10() that generates a uniform random integer in the range [1, 10]. 
You can only call the API rand7(), and you shouldn't call any other API. 
Please do not use a language's built-in random API.

Each test case will have one internal argument n, 
the number of times that your implemented function rand10() will be called while testing. 
Note that this is not an argument passed to rand10().

 

Example 1:
Input: n = 1
Output: [2]

Example 2:
Input: n = 2
Output: [2,8]

Example 3:
Input: n = 3
Output: [3,8,10]

'''


#if randN() can generate a uniform random integer in the range [1, N]
#then (randX() - 1)*Y +randY() can generate uniform random integer in the range[1,XY]

class Solution:
    def rand10(self):
        """
        :rtype: int
        """
        a = rand7()
        b = rand7()
        num = (a-1)*7 + b
        #[1,49]
        if num <=40:
            return num%10+1
        
        #To increase the probability
        a = num-40 #rand9()
        b = rand7()
        num = (a-1)*7+b
        #[1,63]
        if num <=60:
            return num%10+1
        
        a = num-60 #rand3()
        b = rand7()
        num = (a-1)*7+b
        if num<=30:
            return num%10+1
