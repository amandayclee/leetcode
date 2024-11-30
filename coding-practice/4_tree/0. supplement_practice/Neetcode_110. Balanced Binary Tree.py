# Definition for a binary tree node.
from typing import Optional

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def isBalanced(self, root: Optional[TreeNode]) -> bool:
        self.is_balance = True
        self.dfs(root)
        
        return self.is_balance

    def dfs(self, node):
        if not node:
            return 0
        
        if not self.is_balance:
            return 0
        
        left_height = self.dfs(node.left)
        right_height = self.dfs(node.right)
        
        if abs(left_height - right_height) > 1:
            self.is_balance = False
            return 0
        
        return max(left_height, right_height) + 1
    
# TC O(n)
# SC O(h)

class Solution:
    def isBalanced(self, root: Optional[TreeNode]) -> bool:
        return self.dfs(root)[0]
    
    def dfs(self, node):
        if not node:
            return [True, 0] # [balanced, height]
        
        left_height, right_height = self.dfs(node.left), self.dfs(node.right)
        balanced = (left_height[0] and right_height[0] and abs(left_height[1] - right_height[1]) <= 1)
        
        return [balanced, max(left_height[1], right_height[1]) + 1]
    
# TC O(n)
# SC O(h)