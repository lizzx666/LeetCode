'''
Given an input string s, reverse the order of the words.

A word is defined as a sequence of non-space characters. The words in s will be separated by at least one space.

Return a string of the words in reverse order concatenated by a single space.

Note that s may contain leading or trailing spaces or multiple spaces between two words. 
The returned string should only have a single space separating the words. 
Do not include any extra spaces.

 

Example 1:

Input: s = "the sky is blue"
Output: "blue is sky the"
Example 2:

Input: s = "  hello world  "
Output: "world hello"
Explanation: Your reversed string should not contain leading or trailing spaces.
Example 3:

Input: s = "a good   example"
Output: "example good a"
Explanation: You need to reduce multiple spaces between two words to a single space in the reversed string.



'''





class Solution:
    #remove extra space
    def trim_spaces(self,s):
        n = len(s)
        left = 0
        right = n-1
        #remove space from beginning
        while left<=right and s[left]==' ':
            left+=1
        while left<=right and s[right]==' ':
            right-=1

        tmp = []
        while left<=right:
            if s[left]!=' ':
                tmp.append(s[left])
            elif tmp[-1]!=' ':
                tmp.append(s[left])

            left+=1
        return tmp
    
    #general reverse function
    def reverse_string(self,nums,left,right):
        while left<right:
            nums[left],nums[right]=nums[right],nums[left]
            left+=1
            right-=1
    
    #reverse every word
    def reverse_each_word(self,nums):
        start = 0
        end = 0
        n = len(nums)
        while start < n:
            while end < n and nums[end]!=' ':
                end+=1
            self.reverse_string(nums,start,end-1)
            start = end+1
            end+=1

    
    def reverseWords(self, s: str) -> str:
        l = self.trim_spaces(s)
        self.reverse_string(l,0,len(l)-1)
        self.reverse_each_word(l)
        return "".join(l)
