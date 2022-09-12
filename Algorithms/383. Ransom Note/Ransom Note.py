'''
Given two strings ransomNote and magazine, return true if ransomNote can be constructed by using the letters from magazine and false otherwise.

Each letter in magazine can only be used once in ransomNote.

 

Example 1:
Input: ransomNote = "a", magazine = "b"
Output: false

Example 2:
Input: ransomNote = "aa", magazine = "ab"
Output: false

Example 3:
Input: ransomNote = "aa", magazine = "aab"
Output: true



'''



class Solution:
    def canConstruct(self, ransomNote: str, magazine: str) -> bool:
        dm = collections.Counter(magazine)
        
        for x in ransomNote:
            value = dm.get(x)
            if value==None or value==0:
                return False
            else:
                dm[x]-=1
        return True
