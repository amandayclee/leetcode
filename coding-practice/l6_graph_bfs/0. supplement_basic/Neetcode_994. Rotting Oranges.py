from collections import deque
from typing import List

class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        ROWS, COLS = len(grid), len(grid[0])
        queue = deque()
        fresh = 0
        
        for row in range(ROWS):
            for col in range(COLS):
                if grid[row][col] == 2:
                    queue.append((row, col))
                elif grid[row][col] == 1:
                    fresh += 1
        
        if fresh == 0:
            return 0
            
        minutes = -1
        directions = [[1, 0], [-1, 0], [0, 1], [0, -1]]
        
        while queue:
            minutes += 1
            for _ in range(len(queue)):
                row, col = queue.popleft()
                
                for dr, dc in directions:
                    new_row = row + dr
                    new_col = col + dc
                    
                    if (min(new_row, new_col) < 0 or
                        new_row >= ROWS or
                        new_col >= COLS or
                        grid[new_row][new_col] != 1):
                        continue
                    
                    grid[new_row][new_col] = 2
                    fresh -= 1
                    queue.append((new_row, new_col))
        
        return minutes if fresh == 0 else -1