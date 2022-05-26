'''

You are given two lists of closed intervals, firstList and secondList, where firstList[i] = [starti, endi] and secondList[j] = [startj, endj]. 
Each list of intervals is pairwise disjoint and in sorted order.

Return the intersection of these two interval lists.

A closed interval [a, b] (with a <= b) denotes the set of real numbers x with a <= x <= b.

The intersection of two closed intervals is a set of real numbers that are either empty or represented as a closed interval. 
For example, the intersection of [1, 3] and [2, 4] is [2, 3].

 

Example 1:
Input: firstList = [[0,2],[5,10],[13,23],[24,25]], secondList = [[1,5],[8,12],[15,24],[25,26]]
Output: [[1,2],[5,5],[8,10],[15,23],[24,24],[25,25]]


Example 2:
Input: firstList = [[1,3],[5,9]], secondList = []
Output: []


'''


class Solution:
    def intervalIntersection(self, firstList: List[List[int]], secondList: List[List[int]]) -> List[List[int]]:
        m = len(firstList)
        n = len(secondList)
        i=j=0
        result = []
        while i<=m-1 and j<=n-1:
            if firstList[i][0] <= secondList[j][0]:
                if firstList[i][1] < secondList[j][0]:
                    i+=1
                elif secondList[j][0] <= firstList[i][1] <= secondList[j][1]:
                    result.append([secondList[j][0], firstList[i][1]])
                    i+=1
            
                else: 
                    result.append([secondList[j][0],secondList[j][1]])
                    j+=1
        
            elif firstList[i][0] > secondList[j][0]:
                if secondList[j][1] < firstList[i][0]:
                    j+=1
            
                elif firstList[i][0] <= secondList[j][1] <= firstList[i][1]:
                    result.append([firstList[i][0],secondList[j][1]])
                    j+=1
 
                else:
                    result.append([firstList[i][0],firstList[i][1]])
                    i+=1

    
        return result 
