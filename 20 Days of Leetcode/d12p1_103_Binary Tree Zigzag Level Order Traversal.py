from collections import deque
from typing import List
from typing import Optional

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def zigzagLevelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        res, direction = [], 1
        q = deque([root] if root else [])
        
        while q:
            level = []
            for i in range(len(q)):
                current_node = q.popleft()
                level.append(current_node.val)
                if current_node.left:
                    q.append(current_node.left)
                if current_node.right:
                    q.append(current_node.right)
            res.append(level[::direction])
            direction *= -1
        return res
    

if __name__ == "__main__":
    solution = Solution()
    
    test_tree = TreeNode(3)
    test_tree.left = TreeNode(9)
    test_tree.right = TreeNode(20)
    test_tree.right.left = TreeNode(15)
    test_tree.right.right = TreeNode(7)

    test_cases = [
        {"input": test_tree, "expected_output": [[3],[20,9],[15,7]]}
    ]
    for test_case in test_cases:
        assert solution.zigzagLevelOrder(test_case["input"]) == test_case["expected_output"]