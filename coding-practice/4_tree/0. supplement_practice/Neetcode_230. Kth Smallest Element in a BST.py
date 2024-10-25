# Definition for a binary tree node.
from typing import Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
        
class Solution:
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        self.k = k
        
        return self.dfs_helper(root)
    
    def dfs_helper(self, root):
        if not root:
            return None
        
        left = self.dfs_helper(root.left)
        if left is not None:
            return left
        self.k -= 1
        if self.k == 0:
            return root.val
        return self.dfs_helper(root.right)