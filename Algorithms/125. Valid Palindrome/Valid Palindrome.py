'''
Given a string s, determine if it is a palindrome, considering only alphanumeric characters and ignoring cases.

Example 1:
Input: s = "A man, a plan, a canal: Panama"
Output: true
Explanation: "amanaplanacanalpanama" is a palindrome.

Example 2:
Input: s = "race a car"
Output: false
Explanation: "raceacar" is not a palindrome.
'''


class Solution:
    def isPalindrome(self, s: str) -> bool:
        s = ''.join(c for c in s if c.isalnum()).lower()
        if s == s[::-1]:
            return True
        else:
            return False
