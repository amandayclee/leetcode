import collections
from typing import List
class Solution:
    def shortestPathAllKeys(self, grid: List[str]) -> int:
        m = len(grid) # y
        n = len(grid[0]) # x
        keys = 0
        seen = # m * n * 2^6
        queue = collections.deque()
        
        