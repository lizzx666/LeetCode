'''
Given a string s, check if it can be constructed by taking a substring of it and appending multiple copies of the substring together.

 

Example 1:
Input: s = "abab"
Output: true
Explanation: It is the substring "ab" twice.

Example 2:
Input: s = "aba"
Output: false

Example 3:
Input: s = "abcabcabcabc"
Output: true
Explanation: It is the substring "abc" four times or the substring "abcabc" twice.

'''

class Solution:
    def repeatedSubstringPattern(self, s: str) -> bool:
        n = len(s)
        next = [0]*n
        j = 0
        for i in range(1,n):
            while j>0 and s[i]!=s[j]:
                j = next[j-1]
            if s[i]==s[j]:
                j+=1
            next[i]=j

        l = next[-1]
        print(next)
        return l!=0 and n%(n-l)==0



class Solution:
    def repeatedSubstringPattern(self, s: str) -> bool:
        return s in (s+s)[1:-1]
