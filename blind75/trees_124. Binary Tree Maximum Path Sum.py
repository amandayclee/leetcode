# Definition for a binary tree node.
from typing import Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
        
class Solution:
    def maxPathSum(self, root: Optional[TreeNode]) -> int:
        self.max_sum = float('-inf')
        self.dfs(root)
        
        return self.max_sum
        
    def dfs(self, node):
        if not node:
            return 0
        
        left = self.dfs(node.left)
        right = self.dfs(node.right)
            
        left = max(left, 0)
        right = max(right, 0)
        
        self.max_sum = max(self.max_sum, node.val + left + right)
        
        return node.val + max(left, right)
    
    # TC O(n)
    # SC O(h)
