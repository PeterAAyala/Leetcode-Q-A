"""
https://leetcode.com/problems/permutations/

Given an array nums of distinct integers, return all the possible permutations. You can return the answer in any order.
"""
class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        res = []
        self.dfs(nums, [], res)
        return res
    
    def dfs(self, arr, path, result):
        if arr == []:
            result.append(path)
            return
        for i in range(len(arr)):
            self.dfs(arr[:i]+arr[i+1:], path+[arr[i]], result)