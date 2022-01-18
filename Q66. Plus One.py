"""
https://leetcode.com/problems/plus-one/

You are given a large integer represented as an integer array digits, 
where each digits[i] is the ith digit of the integer. 
The digits are ordered from most significant to least significant 
in left-to-right order. The large integer does not contain any leading 0's.

Increment the large integer by one and return the resulting array of digits.
"""

class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        if len(digits) == 0:
            digits =  [1]
        elif digits[-1] == 9:
            digits = self.plusOne(digits[:-1])
            digits.extend([0])
        else:
            digits[-1] += 1
        return digits