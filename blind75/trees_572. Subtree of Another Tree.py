# Definition for a binary tree node.
from collections import deque
from typing import Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
        
class Solution:
    def isSubtree(self, root: Optional[TreeNode], subRoot: Optional[TreeNode]) -> bool:
        if not root:
            return False
        
        if self.is_same_tree(root, subRoot):
            return True
        
        return self.isSubtree(root.left, subRoot) or self.isSubtree(root.right, subRoot)

    # def is_same_tree(self, p, q):
    #     if not p or not q:
    #         return p == q
        
    #     return p.val == q.val and self.is_same_tree(p.left, q.left) and self.is_same_tree(p.right, q.right)
    

# TC O(m * n) m = main tree nodes, n = subtree node
# SC O(h) h = main tree heifght


    def is_same_tree(self, p, q):
        if not p or not q:
            return p == q

        p_queue, q_queue = deque([p]), deque([q])

        while p_queue and q_queue:
            if len(p_queue) != len(q_queue):
                return False

            p_node = p_queue.popleft()
            q_node = q_queue.popleft()

            if p_node.val != q_node.val:
                return False

            if p_node.left and q_node.left:
                p_queue.append(p_node.left)
                q_queue.append(q_node.left)
            elif p_node.left or q_node.left:
                return False

            if p_node.right and q_node.right:
                p_queue.append(p_node.right)
                q_queue.append(q_node.right)
            elif p_node.right or q_node.right:
                return False

        return True
    
# TC O(m * n)
# SC O(min(h, w)) is sub tree -> height, bfs -> w = n/2