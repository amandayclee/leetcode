from typing import List


class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        visit = set()
        island_max = 0
        
        for row in range(len(grid)):
            for col in range(len(grid[0])):                
                if grid[row][col] == 1 and (row, col) not in visit:
                    area = self.dfs(grid, row, col, visit)
                    island_max = max(island_max, area)
                    
        return island_max
    
    def dfs(self, grid, row, col, visit):
        ROWS, COLS = len(grid), len(grid[0])
        
        if (min(row, col) < 0 or row >= ROWS or col >= COLS
            or grid[row][col] != 1
            or (row, col) in visit):
            return 0
        
        visit.add((row, col))
        
        if grid[row][col] == 1:
            return 1 + (self.dfs(grid, row + 1, col, visit) +
                       self.dfs(grid, row - 1, col, visit) +
                       self.dfs(grid, row, col + 1, visit) +
                       self.dfs(grid, row, col - 1, visit))