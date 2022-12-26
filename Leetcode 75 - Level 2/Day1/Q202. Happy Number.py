'''
Write an algorithm to determine if a number n is happy.

A happy number is a number defined by the following process:

Starting with any positive integer, replace the number by the sum of the squares of its digits.
Repeat the process until the number equals 1 (where it will stay), or it loops endlessly in a cycle which does not include 1.
Those numbers for which this process ends in 1 are happy.
Return true if n is a happy number, and false if not.
'''

class Solution:
    def isHappy(self, n: int) -> bool:
        happy = False
        prevTotals = set()
        while not happy:
            total = 0
            for digit in str(n):
                total += int(digit) ** 2
            if total == 1:
                happy = True
                break
            if total in prevTotals:
                break
            prevTotals.add(total)
            n = total
        return happy
            