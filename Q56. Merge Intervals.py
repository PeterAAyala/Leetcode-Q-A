"""
Q56. Merge Intervals
https://leetcode.com/problems/merge-intervals/

Given an array of intervals where intervals[i] = [starti, endi], merge all overlapping intervals, and return an array of the non-overlapping intervals that cover all the intervals in the input.

O(n log n) because we sort the original array
"""

class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        result = []
        
        intervals.sort(key = self.sortByStart)
        for pair in intervals:
            if result and pair[0] <= result[-1][1]:
                newInterval = [result[-1][0], max(pair[1], result[-1][1])] 
                result[-1] = newInterval
            else: 
                result.append(pair)
        return result
        
    def sortByStart(self, pair: List[int]) -> int:
        return pair[0]