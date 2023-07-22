'''

Given n non-negative integers representing an elevation map where the width of each bar is 1, compute how much water it can trap after raining.

 
Example 1:
Input: height = [0,1,0,2,1,0,1,3,2,1,2,1]
Output: 6
Explanation: The above elevation map (black section) is represented by array [0,1,0,2,1,0,1,3,2,1,2,1]. In this case, 6 units of rain water (blue section) are being trapped.


Example 2:
Input: height = [4,2,0,3,2,5]
Output: 9

'''




class Solution:
    def trap(self, height: List[int]) -> int:
        stk = [0]
        res = 0
        if len(height)==1:
            return res
        
        for i in range(1,len(height)):
            if height[i]<height[stk[-1]]:
                stk.append(i)
            elif height[i]==height[stk[-1]]:
                stk.pop()
                stk.append(i)    
            else:
                while stk and height[i]>height[stk[-1]]:
                    mid = height[stk[-1]]
                    stk.pop()
                    if stk:
                        h = min(height[i],height[stk[-1]])-mid 
                        w = i - stk[-1] -1
                        a=h*w
                        res+=a

                stk.append(i)

        return res
