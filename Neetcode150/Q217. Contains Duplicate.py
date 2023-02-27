"""
Q217. Contains Duplicate
https://leetcode.com/problems/contains-duplicate/description/

Given an integer array nums, return true if any value appears at least twice in the array, and return false if every element is distinct.
"""
class Solution:
    # Time complexity: O(n). Worst case, iterate through every element in List nums
    # Space complexity: O(n). Worse case, add every number to the newly created Set. 
    # Approach for O(1) space complexity: Sort the original list first and then iterate through the list to see if there are any duplicates. Has O(n log n) time complexity to sort the list. 
    def containsDuplicate(self, nums: List[int]) -> bool:
        distinctNums = set()
        for num in nums:
            if num in distinctNums:
                return True
            distinctNums.add(num)
        return False
            