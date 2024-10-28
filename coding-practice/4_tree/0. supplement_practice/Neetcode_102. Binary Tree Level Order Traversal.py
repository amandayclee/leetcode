from collections import deque
from typing import List, Optional

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        queue = deque()
        result = []
        
        if root:
            queue.append(root)
            
        while queue:
            level_size = len(queue)
            curr_level = []
            
            for _ in range(level_size):
                curr = queue.popleft()
                curr_level.append(curr.val)
                
                if curr.left:
                    queue.append(curr.left)
                if curr.right:
                    queue.append(curr.right)
                    
            result.append(curr_level)
        
        return result