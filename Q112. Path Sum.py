"""
https://leetcode.com/problems/path-sum/

Given the root of a binary tree and an integer targetSum, return true if the tree has a root-to-leaf path such that adding up all the values along the path equals targetSum.

A leaf is a node with no children.
O(N) runtime, where N is number of nodes in binary tree. Must iterate through every node to see if path exists 
O(N) memory, as recursive call is performed and whole tree can be in memory
"""

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def hasPathSum(self, root: Optional[TreeNode], targetSum: int) -> bool:
        if not root:
            return False
        
        newTarget = targetSum - root.val
        if newTarget == 0 and not root.left and not root.right:
            return True
        else:
            return self.hasPathSum(root.left, newTarget) or                                              self.hasPathSum(root.right, newTarget)
        