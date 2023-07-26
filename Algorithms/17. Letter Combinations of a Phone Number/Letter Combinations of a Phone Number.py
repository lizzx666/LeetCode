'''


Given a string containing digits from 2-9 inclusive, return all possible letter combinations that the number could represent. 
Return the answer in any order.

A mapping of digits to letters (just like on the telephone buttons) is given below. Note that 1 does not map to any letters.


 

Example 1:
Input: digits = "23"
Output: ["ad","ae","af","bd","be","bf","cd","ce","cf"]

Example 2:
Input: digits = ""
Output: []

Example 3:
Input: digits = "2"
Output: ["a","b","c"]


'''



class Solution:
    def __init__(self):
        self.letterMap = [
            "",     # 0
            "",     # 1
            "abc",  # 2
            "def",  # 3
            "ghi",  # 4
            "jkl",  # 5
            "mno",  # 6
            "pqrs", # 7
            "tuv",  # 8
            "wxyz"  # 9
        ]
        self.result = []
        self.s = ""

    def backtracking(self,digits,index,s):
        #if index == len(digits):
        if len(self.s)==len(digits):
            self.result.append(self.s)
            return
        digit = int(digits[index])
        letter = self.letterMap[digit]
        for i in range(len(letter)):
            self.s+=letter[i]
            self.backtracking(digits,index+1,self.s)
            self.s = self.s[:-1]

    def letterCombinations(self, digits: str) -> List[str]:
        if len(digits)==0:
            return self.result
        self.backtracking(digits,0,self.s)
        return self.result
