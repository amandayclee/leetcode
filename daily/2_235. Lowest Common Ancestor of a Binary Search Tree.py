# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        current_node = root
        while current_node:
            if p.val < current_node.val and q.val < current_node.val:
                current_node = current_node.left
            elif p.val > current_node.val and q.val > current_node:
                current_node = current_node.right
            else:
                return current_node