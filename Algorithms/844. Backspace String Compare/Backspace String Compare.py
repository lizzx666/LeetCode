'''
Example 1:
Input: s = "ab#c", t = "ad#c"
Output: true
Explanation: Both s and t become "ac".

Example 2:
Input: s = "ab##", t = "c#d#"
Output: true
Explanation: Both s and t become "".

Example 3:
Input: s = "a#c", t = "b"
Output: false
Explanation: s becomes "c" while t becomes "b".

'''


class Solution:
    def backspaceCompare(self, s: str, t: str) -> bool:
        back = lambda res, c: res[:-1] if c=='#' else res+c
        return reduce(back, s, "")==reduce(back, t, "")
