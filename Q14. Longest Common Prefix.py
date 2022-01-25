"""
https://leetcode.com/problems/longest-common-prefix/

Write a function to find the longest common prefix string amongst an array of strings.
If there is no common prefix, return an empty string "".

O(N*S), where N is number of words in strs and S is length of strs[0]
O(1) memory 

"""

class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        # Start with flower, check is list[1] = 'flower'
        # if not, flower -> flowe, check again, if not, flowe -> flow
        # repeat until either reach end of list or prefix == ""
        
        prefix = strs[0]
        
        for i in range(1, len(strs)):
            match = False
            while not match:
                if prefix == "":
                    break
                if strs[i][:len(prefix)] == prefix:
                    match = True
                else:
                    prefix = prefix[:-1]
        return prefix