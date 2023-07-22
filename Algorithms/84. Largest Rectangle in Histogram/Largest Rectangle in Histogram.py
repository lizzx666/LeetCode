'''

Given an array of integers heights representing the histogram's bar height where the width of each bar is 1, return the area of the largest rectangle in the histogram.

 

Example 1:
Input: heights = [2,1,5,6,2,3]
Output: 10
Explanation: The above is a histogram where width of each bar is 1.
The largest rectangle is shown in the red area, which has an area = 10 units.


Example 2:
Input: heights = [2,4]
Output: 4



'''




class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:

        if len(heights)==1:
            return heights[0]

        res = 0
        stk = [0]
        heights.insert(0,0)
        heights.append(0)
        
        for i in range(1,len(heights)):
            if heights[i]>heights[stk[-1]]:
                stk.append(i)
            elif heights[i]==heights[stk[-1]]:
                stk.pop()
                stk.append(i)
            else:
                while stk and heights[i]<heights[stk[-1]]:
                    mid = stk[-1]
                    stk.pop()
                    if stk:
                        w = i-stk[-1]-1
                        h = heights[mid]
                        res = max(res,h*w)
                stk.append(i)
        return res
