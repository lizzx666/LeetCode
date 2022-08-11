'''
Implement strStr().

Return the index of the first occurrence of needle in haystack, or -1 if needle is not part of haystack.

Clarification:

What should we return when needle is an empty string? This is a great question to ask during an interview.

For the purpose of this problem, we will return 0 when needle is an empty string. This is consistent to C's strstr() and Java's indexOf().

 

Example 1:

Input: haystack = "hello", needle = "ll"
Output: 2
Example 2:

Input: haystack = "aaaaa", needle = "bba"
Output: -1
Example 3:

Input: haystack = "", needle = ""
Output: 0

'''



class Solution:
    def strStr(self, haystack: str, needle: str) -> int:
        a = len(needle)
        b = len(haystack)
        if a==0:
            return 0
        next = self.getnext(needle)
        j = 0
        for i in range(b):
            while j>0 and needle[j]!=haystack[i]:
                j = next[j-1]
            if needle[j]==haystack[i]:
                j+=1
            if j==a:
                return i-a+1
        return -1
                
        
    def getnext(self,needle):
        n = len(needle)
        next = [0]*n
        j = 0
        for i in range(1,n):
            while j>0 and needle[i]!=needle[j]:
                j = next[j-1]
            if needle[i]==needle[j]:
                j+=1
            next[i]=j
        return next
       
       


class Solution:
    def strStr(self, haystack: str, needle: str) -> int:
        if needle == "":
            return 0
        s = len(needle)
        t = len(haystack)
        if s > t:
            return -1
        if s == t and needle == haystack:
            return 0

        for i in range(0,t-s+1):
            if haystack[i:i+s] == needle:
                return i
                break
        return -1
       
       
#better solution      
class Solution:
    def strStr(self, haystack: str, needle: str) -> int:
        for i in range(len(haystack) - len(needle)+1):
            if haystack[i:i+len(needle)] == needle:
                return i
        return -1
