"""
Given the root of a binary tree, return all root-to-leaf paths in any order.

A leaf is a node with no children.
"""

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def binaryTreePaths(self, root: Optional[TreeNode]) -> List[str]:
        if not root:
            return []
        
        result = []
        self.search(root, "", result)
        return result
    
    def search(self, start, current_string, res):
        current_string += str(start.val)
        
        if not start.left and not start.right:
            res.append(current_string)
        if start.left:
            self.search(start.left, current_string + '->', res)
        if start.right:
            self.search(start.right, current_string + '->', res)
            
        