# Definition for a binary tree node.
from typing import List, Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
        
class Solution:
    def inorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        self.res = []
        self.dfs(root)
        
        return self.res
    
    def dfs(self, root):
        if not root:
            return None
        
        self.dfs(root.left)
        self.res.append(root.val)
        self.dfs(root.right)