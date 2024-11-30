# Definition for a binary tree node.
from typing import Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
        
class Solution:
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        self.count = 0
        self.dfs(root)
        
        return self.count
        
    def dfs(self, node):
        if not node:
            return 0
        
        left_height = self.dfs(node.left)
        right_height = self.dfs(node.right)
        
        self.count = max(self.count, left_height + right_height)
        
        return max(left_height, right_height) + 1 # add node itself
    
# TC O(n)
# SC O(h)