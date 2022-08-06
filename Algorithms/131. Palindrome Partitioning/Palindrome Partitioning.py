'''


Given a string s, partition s such that every substring of the partition is a palindrome. Return all possible palindrome partitioning of s.

A palindrome string is a string that reads the same backward as forward.

 

Example 1:
Input: s = "aab"
Output: [["a","a","b"],["aa","b"]]

Example 2:
Input: s = "a"
Output: [["a"]]



'''



class Solution:
    def partition(self, s: str) -> List[List[str]]:
        path = []
        result = []

        def palindrome(s,left,right):
            while left<=right:
                if s[left]!=s[right]:
                    return False
                left+=1
                right-=1
            return True

        def backtracking(s,startindex):
            if startindex>=len(s):
                result.append(path[:])
                return
            for i in range(startindex,len(s)):
                if palindrome(s,startindex,i):
                    path.append(s[startindex:i+1])
                    backtracking(s,i+1)
                    path.pop()
                else:
                    continue
                
                
        backtracking(s,0)
        return result
