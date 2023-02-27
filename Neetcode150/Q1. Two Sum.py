"""
Q1. Two Sum
https://leetcode.com/problems/two-sum/description/

Given an array of integers nums and an integer target, return indices of the two numbers such that they add up to target.

You may assume that each input would have exactly one solution, and you may not use the same element twice.

You can return the answer in any order.
"""
class Solution:
    """ Naive solution: For each element x in Nums, iterate through remaining numbers y in Nums to see if x + y = target. This is O(n^2) time complexity.

    def twoSum(self, nums: List[int], target: int) -> List[int]:
        for i in range(len(nums)):
            for j in range(i+1, len(nums)):
                if nums[i] + nums[j] == target:
                    return [i,j]
        return []
    """
    # Moderately improved solution: Sort the list first into ascending order. Then two points, one and the beginning and another at the end, and adjust one pointer up or down to get closer to the targer. 
    # Time complexity O(nlogn) to sort and O(n) to iterate
    # Space complexity: O(1). 

    # Improved solution. Keep a running list of (value, idx) pairs you have previously iterated on. If the needed complement has already been visited, return the two idices. If not, add it.
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        prevVisited = {}
        for (i, x) in enumerate(nums):
            complement = target - x
            if complement in prevVisited:
                return [prevVisited[complement], i]
            prevVisited[nums[i]] = i


            