'''


Given a pattern and a string s, find if s follows the same pattern.

Here follow means a full match, such that there is a bijection between a letter in pattern and a non-empty word in s.

 

Example 1:
Input: pattern = "abba", s = "dog cat cat dog"
Output: true

Example 2:
Input: pattern = "abba", s = "dog cat cat fish"
Output: false

Example 3:
Input: pattern = "aaaa", s = "dog cat cat dog"
Output: false
'''



class Solution:
    def wordPattern(self, pattern: str, s: str) -> bool:
        mapchar = {}
        mapword = {}
        
        words = s.split(" ")
        if len(words)!=len(pattern):
            return False
        
        for c,w in zip(pattern,words):
            if c not in mapchar:
                if w in mapword:
                    return False
                
                else:
                    mapchar[c] = w
                    mapword[w] = c
            
            else:
                if mapchar[c] != w:
                    return False
        return True
