"""
https://leetcode.com/problems/length-of-last-word/

Given a string s consisting of some words separated by some number of spaces, 
return the length of the last word in the string.

A word is a maximal substring consisting of non-space characters only.
"""


class Solution:
    def lengthOfLastWord(self, s: str) -> int:
        if len(s) == 1:
            return 1 
        
        return self.loop(s, "")
        
    def loop(self, substring, curr):
        if not substring:
            return len(curr)
        lastChar = substring[-1]
        if lastChar == " " and curr != "":
            return len(curr)
        elif lastChar == " " and curr == "":
            return self.loop(substring[:-1], "")
        else:
            curr = curr + lastChar
            return self.loop(substring[:-1], curr)
        
        