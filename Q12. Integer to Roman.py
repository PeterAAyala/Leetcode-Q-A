"""
Given an integer, convert it to a roman numeral.
https://leetcode.com/problems/integer-to-roman/
"""

class Solution:
    def intToRoman(self, num: int) -> str:
        
        lookup = {
            1000: 'M',
            900: 'CM',
            500: 'D',
            400: 'CD',
            100: 'C',
            90: 'XC',
            50: 'L',
            40: 'XL',
            10: 'X',
            9: 'IX',
            5: 'V',
            4: 'IV',
            1: 'I'
        }
        
        res = ""
        for i in lookup:
            res += (num//i) * lookup[i]
            num %= i
        
        return res