'''
Given two strings s and t, return true if t is an anagram of s, and false otherwise.

Example 1:
Input: s = "anagram", t = "nagaram"
Output: true

Example 2:
Input: s = "rat", t = "car"
Output: false

'''

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
