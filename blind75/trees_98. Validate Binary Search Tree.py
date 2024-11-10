# Definition for a binary tree node.
from collections import deque
from typing import Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
        
class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        return self.check_valid(root, float('-inf'), float('inf'))
        
    def check_valid(self, node, min_val, max_val):
        if not node:
            return True
        
        if not min_val < node.val < max_val:
            return False
        
        return self.check_valid(node.left, min_val, node.val) and \
               self.check_valid(node.right, node.val, max_val)

# TC O(n)
# SC O(h)

        
def isValidBST(self, root: Optional[TreeNode]) -> bool:
    if not root:
        return True
        
    queue = deque([(root, float('-inf'), float('inf'))])
    
    while queue:
        node, min_val, max_val = queue.popleft()
        
        if not min_val < node.val < max_val:
            return False
        
        if node.left:
            queue.append((node.left, min_val, node.val))
            
        if node.right:
            queue.append((node.right, node.val, max_val))
    
    return True

# TC O(n)
# SC O(w)