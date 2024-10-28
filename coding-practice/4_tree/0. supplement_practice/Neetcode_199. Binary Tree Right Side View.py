# Definition for a binary tree node.
from collections import deque
from typing import List, Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
        
class Solution:
    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:
        queue = deque()
        res = []
        
        if root:
            queue.append(root)
        
        while queue:
            level = len(queue)
            current_level = []
            
            for _ in range(level):
                curr = queue.popleft()
                current_level.append(curr.val)
            
                if curr.left:
                    queue.append(curr.left)
                if curr.right:
                    queue.append(curr.right)
            res.append(current_level[-1])
    
        return res