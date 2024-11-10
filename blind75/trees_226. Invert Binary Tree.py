# Definition for a binary tree node.
from typing import Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
        
class Solution:
    def invertTree(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        if not root:
            return None
        
        temp_left = root.left
        temp_right = root.right
        
        root.left = self.invertTree(temp_right)
        root.right = self.invertTree(temp_left)
        
        return root
    
# TC O(n)
# SC O(h)