'''

Given an array of integers temperatures represents the daily temperatures, 
return an array answer such that answer[i] is the number of days you have to wait after the ith day to get a warmer temperature. 
If there is no future day for which this is possible, keep answer[i] == 0 instead.

 

Example 1:
Input: temperatures = [73,74,75,71,69,72,76,73]
Output: [1,1,4,2,1,1,0,0]

Example 2:
Input: temperatures = [30,40,50,60]
Output: [1,1,1,0]

Example 3:
Input: temperatures = [30,60,90]
Output: [1,1,0]


'''



class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        stk = [0]
        res = [0]*len(temperatures)


        for i in range(1,len(temperatures)):
            if temperatures[i]<=temperatures[stk[-1]]:
                stk.append(i)
            else:
                while stk and temperatures[i]>temperatures[stk[-1]]:
                    res[stk[-1]]=i-stk[-1]
                    stk.pop()
                stk.append(i)

        return res
