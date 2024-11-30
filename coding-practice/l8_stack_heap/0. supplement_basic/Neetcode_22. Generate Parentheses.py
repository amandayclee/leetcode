from typing import List


class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        # only add open paranthesis if open < n
        # only add a closing paranthesis if closed < open
        # valid if open == closed == n
        
        stack = []
        res = []
        
        self.dfs_backtracking(stack, res, n, 0, 0)
        
        return res
    
    def dfs_backtracking(self, stack, res, n, open_count, closed_count):
        if open_count == closed_count == n:
            res.append("".join(stack))
            return
        
        if open_count < n:
            stack.append("(")
            self.dfs_backtracking(stack, res, n, open_count + 1, closed_count)
            stack.pop()
        
        if closed_count < open_count:
            stack.append(")")
            self.dfs_backtracking(stack, res, n, open_count, closed_count + 1)
            stack.pop()
            
# TC O(4 * n / sqrt(n))
# SC O(2n)