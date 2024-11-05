import heapq
from typing import List


class Solution:
    def minTimeToReach(self, moveTime: List[List[int]]) -> int:
        rows, cols = len(moveTime), len(moveTime[0])
        heap = [(0 ,0, 0, True)]  
        
        visited = [[False] * cols for _ in range(rows)]
        
        directions = [(0, 1), (1, 0), (-1, 0), (0, -1)]
        
        while heap:
            time, cur_row, cur_col, is_odd = heapq.heappop(heap)
            
            if cur_row == rows - 1 and cur_col == cols - 1:
                return time
            
            for dr, dc in directions:
                new_row, new_col = cur_row + dr, cur_col + dc
                
                if (new_row < 0 or new_col < 0 or 
                    new_row >= rows or new_col >= cols or 
                    visited[new_row][new_col]):
                    continue
                
                move_cost = 1 if is_odd else 2
                
                visited[new_row][new_col] = True
                

                new_time = max(moveTime[new_row][new_col], time) + move_cost
                heapq.heappush(heap, (new_time, new_row, new_col, not is_odd))
        
        return -1