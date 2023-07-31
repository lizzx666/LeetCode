'''

A valid IP address consists of exactly four integers separated by single dots. Each integer is between 0 and 255 (inclusive) and cannot have leading zeros.

For example, "0.1.2.201" and "192.168.1.1" are valid IP addresses, but "0.011.255.245", "192.168.1.312" and "192.168@1.1" are invalid IP addresses.
Given a string s containing only digits, return all possible valid IP addresses that can be formed by inserting dots into s. 
You are not allowed to reorder or remove any digits in s. You may return the valid IP addresses in any order.

 

Example 1:

Input: s = "25525511135"
Output: ["255.255.11.135","255.255.111.35"]
Example 2:

Input: s = "0000"
Output: ["0.0.0.0"]
Example 3:

Input: s = "101023"
Output: ["1.0.10.23","1.0.102.3","10.1.0.23","10.10.2.3","101.0.2.3"]


'''



class Solution:
    def restoreIpAddresses(self, s: str) -> List[str]:
        res = []
        cur = []
        self.backtracking(s,0,cur,res)
        return res
    
    def backtracking(self,s,start_index,cur,res):
        if start_index==len(s) and len(cur)==4:
            res.append('.'.join(cur))
            return
        if len(cur) > 4:
            return
        
        for i in range(start_index,min(start_index+3,len(s))): #at most 255
            if self.isvalid(s,start_index,i):
                sub = s[start_index:i+1]
                cur.append(sub)
                print(cur)
                self.backtracking(s,i+1,cur,res)
                cur.pop()

    def isvalid(self,s,start,end):
        if start>end:
            return False
        if s[start]=='0' and start!=end: #single 0 is valid but start with 0 is invalid
            return False
        num = int(s[start:end+1])
        return 0<=num<=255

