"""
347. Top K Frequent Elements
https://leetcode.com/problems/top-k-frequent-elements/description/

Given an integer array nums and an integer k, return the k most frequent elements. You may return the answer in any order.
"""
# O(n log n) time, O(n) space complexity
class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        # First create mapping of 
        # O(n) time complexity, O(n) space
        h = {}
        for num in nums:
            if num not in h:
                h[num] = 1
            else:
                h[num] += 1
        # Create a list of tuples, where each number has count of appearances
        # O(n) time complexity, O(n) space
        res = []
        for num in h:
            res.append([num, h[num]])
        
        # Sort the resulting list descending by counts
        # O(nlogn) time complexity, O(1) space
        res.sort(reverse = True, key = lambda x: x[1])
        
        # Grab just the relevant numbers to return
        result = []
        for i in range(k):
            result.append(res[i][0])
        return result