
from collections import deque

# Find the length of the shortest path from top left of the grid to the bottom right.

class Solution:
    def problem(self, grid):
        visit = set()
        queue = deque()
        return self.bfs(grid, visit, queue)

    def bfs(self, grid, visit, queue):
        ROWS, COLS = len(grid), len(grid[0])
        
        queue.append((0, 0))
        visit.add((0, 0))
        
        directions = [[1, 0], [-1, 0], [0, 1], [0, -1]] 
        
        length = 0
        
        while queue:
            for _ in range(len(queue)):
                row, col = queue.popleft()
                
                if row == ROWS - 1 and col == COLS - 1:
                    return length
                
                for dr, dc in directions:
                    new_row = row + dr
                    new_col = col + dc

                    if (min(new_row, new_col) < 0 or 
                        new_row >= ROWS or 
                        new_col >= COLS or
                        grid[new_row][new_col] == 1 or
                        (new_row, new_col) in visit):
                        continue
                    
                    queue.append((new_row, new_col))
                    visit.add((new_row, new_col))
                    
            length += 1
        
        return -1
