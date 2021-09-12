'''
Given a string s, find the first non-repeating character in it and return its index. If it does not exist, return -1.
 

Example 1:
Input: s = "leetcode"
Output: 0

Example 2:
Input: s = "loveleetcode"
Output: 2

Example 3:
Input: s = "aabb"
Output: -1
'''


class Solution:
    def firstUniqChar(self, s: str) -> int:
        import string
        letters = string.ascii_lowercase
        index_s = [s.index(l) for l in letters if s.count(l)==1]
        return min(index_s) if len(index_s) > 0 else -1
