'''
Given two strings s and t, return true if t is an anagram of s, and false otherwise.

Example 1:
Input: s = "anagram", t = "nagaram"
Output: true

Example 2:
Input: s = "rat", t = "car"
Output: false

'''




class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        check = [0]*26
        for i in range(len(s)):
            check[ord(s[i])-ord('a')]+=1
        
        for i in range(len(t)):
            check[ord(t[i])-ord('a')]-=1
        
        for i in range(26):
            if check[i]!=0:
                return False
        return True

#method 1
class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        from collections import Counter
        s1 = Counter(s)
        t1 = Counter(t)
        return s1==t1
      
#method 2
class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        return sorted(s) == sorted(t)
