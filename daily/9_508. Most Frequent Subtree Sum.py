# Definition for a binary tree node.
from typing import List, Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
        
class Solution:
    def findFrequentTreeSum(self, root: Optional[TreeNode]) -> List[int]:
        frequency = {}
        self.dfs(root, frequency)
        max_freq = max(frequency.values())
        result = [key for key, value in frequency.items() if value == max_freq]
        
        return result
        
    def dfs(self, node, frequency):
        if not node:
            return 0
        
        left_sum = self.dfs(node.left, frequency)
        right_sum = self.dfs(node.right, frequency)
        
        curr_sum = node.val + left_sum + right_sum
        
        frequency[curr_sum] = frequency.get(curr_sum, 0) + 1
        
        return curr_sum
    
# TC O(N)
# SP O(H) + O(N) = O(N)