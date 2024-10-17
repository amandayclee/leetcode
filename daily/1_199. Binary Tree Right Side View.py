from typing import List, Optional

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:
        result = []
        self.dfs(root, 0, result)
        return result
    
    def dfs(self, node: Optional[TreeNode], level: int, result: List[int]) -> None:
        if not node:
            return
        
        if level == len(result):
            result.append(node.val)
        
        self.dfs(node.right, level + 1, result)
        self.dfs(node.left, level + 1, result)
        