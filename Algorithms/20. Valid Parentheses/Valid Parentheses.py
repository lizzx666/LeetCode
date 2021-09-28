'''
Given a string s containing just the characters '(', ')', '{', '}', '[' and ']', determine if the input string is valid.

An input string is valid if:

Open brackets must be closed by the same type of brackets.
Open brackets must be closed in the correct order.
 

Example 1:
Input: s = "()"
Output: true

Example 2:
Input: s = "()[]{}"
Output: true

Example 3:
Input: s = "(]"
Output: false

Example 4:
Input: s = "([)]"
Output: false

Example 5:
Input: s = "{[]}"
Output: true
'''

#method 1:
class Solution:
    def isValid(self, s: str) -> bool:
        while "()" in s or "{}" in s or "[]" in s:
            s = s.replace("()","").replace("{}","").replace("[]","")
        return s == ''

#method 2:
class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        dict_1 = {"]":"[",")":"(","}":"{"}
        for char in s:
            if char in dict_1.values():
                stack.append(char)
            elif char in dict_1.keys():
                if stack == [] or dict_1[char] != stack.pop():
                    return False
            else:
                return False
        return stack == []
