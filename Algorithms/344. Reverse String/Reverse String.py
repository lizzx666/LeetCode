'''
Write a function that reverses a string. The input string is given as an array of characters s.


Example 1:
Input: s = ["h","e","l","l","o"]
Output: ["o","l","l","e","h"]

Example 2:
Input: s = ["H","a","n","n","a","h"]
Output: ["h","a","n","n","a","H"]


'''



class Solution:
    def reverseString(self, s: List[str]) -> None:
        """
        Do not return anything, modify s in-place instead.
        """
        head = 0
        tail = len(s)-1
        while head <= tail:
            s[head], s[tail] = s[tail], s[head]
            head += 1
            tail -= 1
