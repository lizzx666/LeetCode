'''
You are given a string s. We want to partition the string into as many parts as possible so that each letter appears in at most one part.

Return a list of integers representing the size of these parts.

 

Example 1:
Input: s = "ababcbacadefegdehijhklij"
Output: [9,7,8]
Explanation:
The partition is "ababcbaca", "defegde", "hijhklij".
This is a partition so that each letter appears in at most one part.
A partition like "ababcbacadefegde", "hijhklij" is incorrect, because it splits s into less parts.

Example 2:
Input: s = "eccbbbbdec"
Output: [10]

'''

class Solution:
    def partitionLabels(self, s: str) -> List[int]:
        dic = {l:index for index,l in enumerate(s)}
        num = 0
        result = []
        j = dic[s[0]]
        
        for i in range(len(s)):
            num += 1
            if dic[s[i]] > j:
                j = dic[s[i]]
            if i==j:
                result.append(num)
                num = 0
        return result
