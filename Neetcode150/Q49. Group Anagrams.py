"""
49. Group Anagrams
https://leetcode.com/problems/group-anagrams/description/

Given an array of strings strs, group the anagrams together. You can return the answer in any order.

An Anagram is a word or phrase formed by rearranging the letters of a different word or phrase, typically using all the original letters exactly once.
"""
class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        h = {}
        for word in strs:
            ordered = "".join(sorted(word))
            if ordered in h:
                h[ordered].append(word)
            else:
                h[ordered] = [word]
        return h.values()