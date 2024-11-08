from typing import List


class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        visit = set()
        islands = 0
        
        for row in range(len(grid)):
            for col in range(len(grid[0])):
                if grid[row][col] == "1" and (row, col) not in visit:
                    islands += 1
                    self.dfs(grid, row, col, visit)
        
        return islands
        
    def dfs(self, grid, row, col, visit):
        ROWS, COLS = len(grid), len(grid[0])
                
        if (min(row, col) < 0 
            or row >= ROWS 
            or col >= COLS 
            or (row, col) in visit
            or grid[row][col] != "1"):
            return
        
        visit.add((row, col))
        
        self.dfs(grid, row + 1, col, visit)
        self.dfs(grid, row - 1, col, visit)
        self.dfs(grid, row, col + 1, visit)
        self.dfs(grid, row, col - 1, visit)
