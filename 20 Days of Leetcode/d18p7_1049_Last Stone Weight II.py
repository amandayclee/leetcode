from typing import List
from math import ceil

class Solution:
    def lastStoneWeightII(self, stones: List[int]) -> int:
        stone_sum = sum(stones)
        target = ceil(stone_sum / 2) # round up
        
        def dfs(i, total):
            if total >= target or i == len(stones):
                return abs(total - (stone_sum - total))
            if (i, total) in memo:
                return memo[(i, total)]
            
            memo[(i, total)] = min(dfs(i + 1, total), dfs(i + 1, total + stones[i]))
            return memo[(i, total)]
        
        memo = {}
        return dfs(0, 0)