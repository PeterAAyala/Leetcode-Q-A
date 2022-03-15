"""
Q15: 3Sum
https://leetcode.com/problems/3sum/

Given an integer array nums, return all the triplets [nums[i], nums[j], nums[k]] such that i != j, i != k, and j != k, and nums[i] + nums[j] + nums[k] == 0.

Notice that the solution set must not contain duplicate triplets.
O(n^2 + n log n) time 
O(1) space
"""

class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        
        # [-2,-2, -2, 0, 4]
        # [-2,-2, -2, -1, 0, 3, 4]
        if len(nums) < 3:
            return []
        
        # O(n log n)
        nums.sort()
        result = []
        for i in range(len(nums) - 2):
            left = i + 1
            right = len(nums) - 1
            if nums[i] == nums[i-1] and i > 0:
                continue
                
            while left < right:
                totalSum = nums[i] + nums[left] + nums[right]
                if totalSum == 0:
                    result.append([nums[i],nums[left],nums[right]])
                    while left < right and nums[left] == nums[left + 1]:
                        left += 1
                    while left < right and nums[right] == nums[right - 1]:
                        right -= 1
                    left +=1
                    right -=1
                if totalSum < 0:
                    left += 1
                if totalSum > 0: 
                    right -= 1
        return result
            
            