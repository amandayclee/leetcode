# Definition for a binary tree node.
from typing import Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
         
class Solution:
    def trimBST(self, root: Optional[TreeNode], low: int, high: int) -> Optional[TreeNode]:
        if not root:
            return None
        
        if root.val < low:
            return self.trimBST(root.right, low, high)
            
        elif root.val > high:
            return self.trimBST(root.left, low, high)
            
        else:
            root.left = self.trimBST(root.left, low, high)
            root.node = self.trimBST(root.right, low, high)
            
            return root
        
# TC O(n) visit every node
# SC O(h) height of the tree / stack #
