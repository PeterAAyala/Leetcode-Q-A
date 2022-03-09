"""
Given a binary tree, find its minimum depth.

The minimum depth is the number of nodes along the shortest path from the root node down to the nearest leaf node.

Note: A leaf is a node with no children.

https://leetcode.com/problems/minimum-depth-of-binary-tree/
"""


# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def minDepth(self, root: Optional[TreeNode]) -> int:
        return self.search(root, 0)
        
    def search(self, root: Optional[TreeNode], counter: int) -> int:
        if not root:
            return counter
        # Reach a node with no other paths down
        if not root.left and not root.right:
            return 1 + counter
        if not root.left:
            return self.search(root.right, counter + 1)
        if not root.right:
            return self.search(root.left, counter + 1)
        return min(self.search(root.left, counter + 1), self.search(root.right, counter + 1))