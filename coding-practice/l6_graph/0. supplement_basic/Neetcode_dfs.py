
class Solution:
    def problem(self, grid):
        visit = set()
        self.dfs(grid, 0, 0, visit)

    def dfs(self,grid, row, col, visit):
        ROWS, COLS = len(grid), len(grid[0])
        if (min(row,col) < 0 or row >= ROWS or col >= COLS 
            or (row, col) in visit 
            or grid[row][col] == 1):
            return 0

        if row == ROWS - 1 and col == COLS - 1:
            return 1
        
        visit.add((row, col))
        
        count = 0
        count += self.dfs(grid, row + 1, col, visit)
        count += self.dfs(grid, row - 1, col, visit)
        count += self.dfs(grid, row, col - 1, visit)
        count += self.dfs(grid, row, col + 1, visit)

        visit.remove((row, col))
        
        return count