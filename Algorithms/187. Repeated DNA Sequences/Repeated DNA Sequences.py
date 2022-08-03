'''

The DNA sequence is composed of a series of nucleotides abbreviated as 'A', 'C', 'G', and 'T'.

For example, "ACGAATTCCG" is a DNA sequence.
When studying DNA, it is useful to identify repeated sequences within the DNA.

Given a string s that represents a DNA sequence, return all the 10-letter-long sequences (substrings) that occur more than once in a DNA molecule. 
You may return the answer in any order.

 

Example 1:
Input: s = "AAAAACCCCCAAAAACCCCCCAAAAAGGGTTT"
Output: ["AAAAACCCCC","CCCCCAAAAA"]

Example 2:
Input: s = "AAAAAAAAAAAAA"
Output: ["AAAAAAAAAA"]


'''



class Solution:
    def findRepeatedDnaSequences(self, s: str) -> List[str]:
        l, n = 10, len(s)
        seen = set()
        output = set()
        
        for i in range(n-l+1):
            tmp = s[i:i+l]
            if tmp in seen:
                output.add(tmp[:])
            seen.add(tmp)
        return output
