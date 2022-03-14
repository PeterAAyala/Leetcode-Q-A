"""
Q242. Valid Anagram 
https://leetcode.com/problems/valid-anagram/

Given two strings s and t, return true if t is an anagram of s, and false otherwise.

An Anagram is a word or phrase formed by rearranging the letters of a different word or phrase, typically using all the original letters exactly once.
"""


class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        availableLetters = {}
        if len(s) != len(t):
            return False
        for letter in s:
            if letter in availableLetters.keys():
                availableLetters[letter] += 1
            else:
                availableLetters[letter] = 1
        for letter in t:
            if letter not in availableLetters.keys():
                return False
            if (availableLetters[letter] - 1 < 0):
                return False
            availableLetters[letter] -= 1
        return True
        