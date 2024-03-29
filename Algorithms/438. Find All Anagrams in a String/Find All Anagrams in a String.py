'''
Given two strings s and p, return an array of all the start indices of p's anagrams in s. You may return the answer in any order.

An Anagram is a word or phrase formed by rearranging the letters of a different word or phrase, typically using all the original letters exactly once.

 

Example 1:

Input: s = "cbaebabacd", p = "abc"
Output: [0,6]
Explanation:
The substring with start index = 0 is "cba", which is an anagram of "abc".
The substring with start index = 6 is "bac", which is an anagram of "abc".

Example 2:
Input: s = "abab", p = "ab"
Output: [0,1,2]
Explanation:
The substring with start index = 0 is "ab", which is an anagram of "ab".
The substring with start index = 1 is "ba", which is an anagram of "ab".
The substring with start index = 2 is "ab", which is an anagram of "ab".

'''


class Solution:
      
    def findAnagrams(self, s: str, p: str) -> List[int]:
        ns, np = len(s), len(p)
        if np>ns:
            return []
        
        result = []

        p_count = Counter(p)
        s_count = Counter()
        
        for i in range(ns):
            s_count[s[i]]+=1
            
            if i>=np:
                if s_count[s[i-np]]==1:
                    del s_count[s[i-np]]
                else:
                    s_count[s[i-np]]-=1
                
            if p_count == s_count:
                result.append(i-np+1)
        return result
