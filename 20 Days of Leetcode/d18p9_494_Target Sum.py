from typing import List

class Solution:
    def findTargetSumWays(self, nums: List[int], target: int) -> int:
        memo = {} # (index, total) -> # of ways
        
        def backtracking(i, total):
            if i == len(nums):
                return 1 if total == target else 0
            if (i, total) in memo:
                return memo[(i, total)]
            
            memo[(i, total)] = (backtracking(i + 1, total + nums[i]) +
                                backtracking(i + 1, total - nums[i]))
            
            return memo[(i, total)]
        
        return backtracking(0, 0)
            