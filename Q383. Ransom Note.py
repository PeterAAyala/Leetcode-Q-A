"""
Q383. Ransom Note
https://leetcode.com/problems/ransom-note/

Given two strings ransomNote and magazine, return true if ransomNote can be constructed from magazine and false otherwise.

Each letter in magazine can only be used once in ransomNote.
"""
class Solution:
    def canConstruct(self, ransomNote: str, magazine: str) -> bool:
        counterDict = {}
        
        for letter in magazine:
            if letter not in counterDict.keys():
                counterDict[letter] = 1
            else:
                counterDict[letter] += 1
        
        for letter in ransomNote:
            
            if letter not in counterDict.keys():
                return False
            if counterDict[letter] == 0:
                return False
            counterDict[letter] -= 1
        
        return True
                