"""
Q20: Valid Parentheses
https://leetcode.com/problems/valid-parentheses/

Given a string s containing just the characters '(', ')', '{', '}', '[' and ']', determine if the input string is valid.

An input string is valid if:

Open brackets must be closed by the same type of brackets.
Open brackets must be closed in the correct order.
"""

class Solution:
    def isValid(self, s: str) -> bool:
        opens = set([ "(", "{", "[" ])
        pairs = {
            "]": "[",
            "}": "{",
            ")": "("
        }
        lastOpen = []
        
        for chara in s:
            if chara in opens:
                lastOpen.append(chara)
            else:
                if len(lastOpen) == 0:
                    return False
                if pairs[chara] == lastOpen[-1]:
                    lastOpen.pop()
                else:
                    return False
        
        if len(lastOpen) > 0:
            return False    
        return True
            